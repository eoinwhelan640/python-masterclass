# very useful importable classes for creating scrollable listboxes based off a sql db
import sqlite3
import tkinter as tk

class Scrollbox(tk.Listbox):

    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)

        self.scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL, command=self.yview)

    # override the default grid method of tkinter
    def grid(self, row, column, sticky="nsw", rowspan=1, columnspan=1, **kwargs):
        # here we're saying explicitly use parent class grid method, avoid the one we're in recursively
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


class DataListBox(Scrollbox):

    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        super().__init__(window, **kwargs)

        self.linked_box = None
        self.link_field = None
        self.link_value = None

        self.cursor = connection.cursor()
        self.table = table
        self.field = field

        # replaces the other bind commands, dont need them anymore
        self.bind('<<ListboxSelect>>', self.on_select)

        self.sql_select = "SELECT " + self.field + ", _id " + "FROM " + self.table
        if sort_order:
            #self.sql_sort = f"ORDER BY  {','.join(sort_order)}"
            self.sql_sort = " ORDER BY " + ",".join(sort_order)
        else:
            self.sql_sort = " ORDER BY " + self.field

    def clear(self):
        self.delete(0, tk.END)

    def link(self, widget, link_field):
        self.linked_box = widget
        widget.link_field = link_field

    def requery(self, link_value=None):
        self.link_value = link_value # store the id, so we know the "master" record we're populated from
        # only execute if there is a link established between listboxes
        if link_value and self.link_field:
            sql = f"{self.sql_select} WHERE {self.link_field}=? {self.sql_sort}"
            print(sql)
            self.cursor.execute(sql, (link_value,))
        else:
            print(self.sql_select + self.sql_sort) #TODO delete this line
            self.cursor.execute(self.sql_select + self.sql_sort)
        # clear the listbox contents before re-loading
        self.clear()
        # execute query and loop over cursor
        for value in self.cursor:
            # value 0 is because we're adding first item of tuple to the list
            self.insert(tk.END, value[0])

        if self.linked_box:
            # make sure when we select a new artist/option, the old ones arent still displayed
            self.linked_box.clear()

    # newer version of get_albums used in class
    def on_select(self, event):
        if self.linked_box and self.curselection():
            print(self is event.widget) # TODO delete this
            index = self.curselection()[0]
            value = self.get(index),

            # get the id from the db row + make sure it's correct one by incl link_value where appropriate
            if self.link_value:
                # new tuple, as they're immutable so cant just add to it
                value = value[0], self.link_value
                sql_where = f" WHERE {self.field}=? AND {self.link_field}=?"
            else:
                sql_where = f" WHERE {self.field}=?"

            link_id = self.cursor.execute(self.sql_select + sql_where, value).fetchone()[1]
            # pass id of artist we wanna display albums for
            self.linked_box.requery(link_id)

if __name__ == '__main__':
    conn = sqlite3.connect("music.sqlite")
    mainWindow = tk.Tk()
    mainWindow.title("Music DB browser")
    mainWindow.geometry("1024x768")


    mainWindow.columnconfigure(0, weight=2)
    mainWindow.columnconfigure(1, weight=2)
    mainWindow.columnconfigure(2, weight=2)
    mainWindow.columnconfigure(3, weight=2) # spacer col on right

    mainWindow.rowconfigure(0, weight=1)
    mainWindow.rowconfigure(1, weight=5) # more weight to middle rows cos they have the listboxes
    mainWindow.rowconfigure(2, weight=5)
    mainWindow.rowconfigure(3, weight=1)


    # labels
    tk.Label(mainWindow, text="Artists").grid(row=0, column=0)
    tk.Label(mainWindow, text="Albums").grid(row=0, column=1)
    tk.Label(mainWindow, text="Songs").grid(row=0, column=2)

    # Artists listbox
    #artistsList = Scrollbox(mainWindow, background="cyan")
    # initially use Scrollbox but then change to our custom class
    artistsList = DataListBox(mainWindow, conn, "artists", "name", background="cyan")
    #def __int__(self, window, connection, table, field, sort_order=(), **kwargs):

    artistsList.grid(row=1, column=0, sticky="nsew", rowspan=2, padx=(30, 0))
    artistsList.config(border=2, relief="sunken")

    # allow the listbox to display results of sql query - initialises the artists list in box
    # for artist in conn.execute("SELECT artists.name FROM artists ORDER BY artists.name"):
    #     artistsList.insert(tk.END, artist[0])
    # insetad of this ^ we can directly call requery
    # Leave this cos we want the artists list populated at first
    artistsList.requery()

    # create an event bound to artists - something to happen when we click on an artist in the box. in this case
    # event is a function to get albums names
    # when a bound function is called it gets passed a single arg, the event.
    #artistsList.bind('<<ListboxSelect>>', get_albums)

    # Setting the scrollbar - class covers this now
    # artistScroll = tk.Scrollbar(mainWindow, orient=tk.VERTICAL, command=artistsList.yview) #yview is scroll on
    #                                                                                         # y axis
    # artistScroll.grid(row=1, column=0, sticky="nse", rowspan=2)
    # artistsList['yscrollcommand'] = artistScroll.set # set the scrolling on the widget to track correctly,
    #                                                 # y scrollcommand is an attribute of the listbox

    # album listbox
    # Variables are tracked variables, when they change, anything using them is notified of the change
    # So the listbox updates when this variable is updated
    albumLV = tk.Variable(mainWindow)
    albumLV.set(("Choose an Artist",))
    albumList = DataListBox(mainWindow, conn, "albums", "name", sort_order=("name",), background="violet")
    #albumList.requery()
    albumList.grid(row=1, column=1, sticky='nsew', padx=(30,))
    albumList.config(border=2, relief="sunken")

    # Once clas sis made, this gets replaced
    #albumList.bind('<<ListboxSelect>>', get_songs)
    artistsList.link(albumList, "artist")
    # Again this is covered in class now
    # albumScroll = tk.Scrollbar(mainWindow, orient=tk.VERTICAL, command=albumList.yview)
    # albumScroll.grid(row=1, column=1, sticky="nse", rowspan=2)
    # albumList['yscrollcommand'] = albumScroll.set


    # Songs listbox
    songsLV = tk.Variable(mainWindow)
    songsLV.set(("Choose an Album",))
    songsList = DataListBox(mainWindow, conn, "songs", "title", ("track","title"), background="orange")
    #songsList.requery()
    songsList.grid(row=1, column=2, sticky="nsew", padx=(30,0))
    songsList.config(border=2, relief="sunken")

    # Once we have class, link these as well. link song list to album list
    albumList.link(songsList, "album")

    mainWindow.mainloop()
    print("Closing database connection")
    conn.close()