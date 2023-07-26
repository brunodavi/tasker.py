from lxml.builder import E

root = E.TaskerData(sr="", dvi="1", tv="6.2.9-rc",
            E.Task(sr="task66",
                   E.cdate("1690327423014"),
                   E.edate("1690338426933"),
                   E.id("66"),
                   E.nme("task"),
                   E.Action(sr="act0", ve="7",
                            E.code("511"),
                            E.Int(sr="arg0", val="0"),
                            E.Str(sr="arg1", ve="3")
                )
           )
        )
