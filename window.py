import tkinter as tk
import xlsxwriter as xls
from tkinter import filedialog
from tkinter import simpledialog

class Window:
    def __init__(self):
        self. dir = "NULL"
        self.root = tk.Tk()
        self.root.geometry("685x600")
        self.root.resizable(False, False)
        self.root.title("Pferde in Balance - Testbogen")
        self.output = []
        self.group1_entries = ["Testampulle für Therapieblockade",
                               "Bindegewebsbelastung allgemein",
                               "funktionelle Störung als Ursache für Beschwerden",
                               "Hinweis für muskuläre Stürungen",
                               "Genetische Ursache für die Störung bzw. Belastung",
                               "Test auf bereits stattfindende morphologische Organveränderungen",
                               "Test auf bereits manifeste degenerative Prozess",
                               "Test auf signifikante Herde in den jeweiligen Organbereichen",
                               "Auffinden des eigentlichen Organproblems, Quelle der Kausalkette",
                               "Test auf streuende Störherde und Störfelder",
                               "Test auf Narbenstörfelder",
                               "Therapieblockaden durch physische Traumata",
                               "Test auf Zahnherde",
                               "Belastung des Organismus durch abgekapselteb Enzündungsherd",
                               "Blockade der Drainage (Ausscheidungsorgane)",
                               "Therapeutische Kontrolle der Mesenchym-Entgiftung",
                               "Test auf zystische Prozesse und Veränderungen der Gewebe"]

        self.group2_entries = ["Allgemeine Belastungen durch Umweltgifte",
                               "Test auf erworbene toxische Informationen",
                               "Test auf ererbte toxische Vergiftungen",
                               "Test auf substantielle Vergiftungen",
                               "Belastung durch Quecksilber-Intoxikation",
                               "verdecktes Amalgam",
                               "Belastung durch überdosierte Arzneimittel (allopathisch)",
                               "Belastung durch Impfungen",
                               "geopathogene Kraftfelder allgeimein",
                               "Symptome durch Umpolung der Links-Rechts-Drehung der Zellen",
                               "Belastung durch radioaktive Strahlung"]

        self.group3_entries = ["Test auf Allergie ohne autoaggressive Reaktion (Allergietyp I)",
                               "Test auf Autoimmunreaktion",
                               "Test auf Immunschwäche - Defizite",
                               "Bakterielle Infektion im allgemeinen (spezifischen Erreger testen!)",
                               "Virale Infektion im allgemeinen (spezifischen Erreger testen)",
                               "Test auf Parasiten im allgemeinen",
                               "Test auf Pilzbefall durch Candida albicans",
                               "Reaktion auf Mischung 1",
                               "Reaktion auf Mischung 2"]

        self.group4_entries = ["Veränderung der Blutzusammensetzung",
                               "Belastung der Organismus durch tierische Eiweisse",
                               "Belastung des Organismus durch freie Radikale",
                               "Störung durch gen-manipulierte Lebensmittel",
                               "Verwertungsstörung",
                               "Störungen im Säuren-Basen-Haushalt - Übersäuerung",
                               "Störungen im Säuren-Basen-Haushalt - alkalische Reaktion",
                               "Belastungen des Organismus durch Stoffwechselträgheit",
                               "bzw. Ampulle Cholesterinum - Test auf erhöhten Cholesterinspiegel",
                               "Phosphat-Unveträglichkeit (Hyperaktivität o.ä)",
                               "Nahrungsmittelunverträglichkeit",
                               "Nahrungsmittelallergie",
                               "Belastungen durch Dickdarmdysbiose",
                               "Belastungen durch Dünndarmdysbiose",
                               "Belastungen durch Genußmittel (Kaffee, Alkohol, Kakao, Nikotin)",
                               "Störungen durch Sauerstoffmangel",
                               "Test auf Spurenelementmangel",
                               "Test auf Mineralienmangel",
                               "Test auf Vitaminmangel",
                               "Test auf Aminosäureungleichgewicht",
                               "Test auf Enzymmangel"]

        self.group5_entries = ["Hinweis auf psychische Belastung",
                               "Test auf Stressreaktionen",
                               "Symptome durch psychosomatische Störung",
                               "Belastung durch Erschöpfung",
                               "Blockierungen durch psychische Traumata",
                               "Störungen durch Dysbalance des vegetativen Nervensystems",
                               "Test auf endokrine Belastung",
                               "Test auf Hormonmangel",
                               "Energieblockade",
                               "durch negative Gedanken blockierte Therapie",
                               "Symptome durch depressive Belasstungen",
                               "Symptome durch endogene Depression"]

        self.group6_entries = ["Belastung des Organismus durch Therapieschäden",
                               "Hinweis für benigne Tumore (gutartige Formen)",
                               "Hinweis für Präcancerosen (Tumore im Anfangsstudium)",
                               "Hinweis für Kanzerose (Makro-Ca.)",
                               "Hinweis für Prämalignosen (bösartige Tumore am Beginn)",
                               "Hinweis für Prä-Diabetes mellitus",
                               "Hinweis auf Hypertonie und deren schädigen Einfluß",
                               "Hinweis auf Hypotonie und deren Unterversorgung der Gewebe",
                               "Chronische behandlungsresistente Ekzeme",
                               "Unklare Herz-/Kreislaufbahnbeschwerden",
                               "allgemeine Leberbelastung",
                               "Störungen des Organismus durch Verhärtungen, Sklerose",
                               "Regenerationsstörung",
                               "Energie- und Regulationsdefizit",
                               "Löschampulle - zeigt den 'wahren' Test-Wert"]

        self.group7_entries = ["Zelle und Gewebe",
                               "Blut",
                               "Immunsystem",
                               "Lymphsystem",
                               "Kreislaufsystem",
                               "Herz",
                               "Atemwege",
                               "Niere",
                               "Verdauungsystem",
                               "Leber/Galle",
                               "Stoffwechsel",
                               "Bewegungsapparat",
                               "Nervensystem",
                               "Sehorgan",
                               "Hörorgan/Gleichgewichtsorgan",
                               "Haut/Fell",
                               "Hormonsystem",
                               "Weibliche Geschlechtsorgane",
                               "Männliche Geschlechtsorgane",
                               "Psyche",
                               "Stress",
                               "Zähne"]

        self.complete_entries =["Testampulle für Therapieblockade",
                               "Bindegewebsbelastung allgemein",
                               "funktionelle Störung als Ursache für Beschwerden",
                               "Hinweis für muskuläre Stürungen",
                               "Genetische Ursache für die Störung bzw. Belastung",
                               "Test auf bereits stattfindende morphologische Organveränderungen",
                               "Test auf bereits manifeste degenerative Prozess",
                               "Test auf signifikante Herde in den jeweiligen Organbereichen",
                               "Auffinden des eigentlichen Organproblems, Quelle der Kausalkette",
                               "Test auf streuende Störherde und Störfelder",
                               "Test auf Narbenstörfelder",
                               "Therapieblockaden durch physische Traumata",
                               "Test auf Zahnherde",
                               "Belastung des Organismus durch abgekapselteb Enzündungsherd",
                               "Blockade der Drainage (Ausscheidungsorgane)",
                               "Therapeutische Kontrolle der Mesenchym-Entgiftung",
                               "Test auf zystische Prozesse und Veränderungen der Gewebe",
                               "Allgemeine Belastungen durch Umweltgifte",
                               "Test auf erworbene toxische Informationen",
                               "Test auf ererbte toxische Vergiftungen",
                               "Test auf substantielle Vergiftungen",
                               "Belastung durch Quecksilber-Intoxikation",
                               "verdecktes Amalgam",
                               "Belastung durch überdosierte Arzneimittel (allopathisch)",
                               "Belastung durch Impfungen",
                               "geopathogene Kraftfelder allgeimein",
                               "Symptome durch Umpolung der Links-Rechts-Drehung der Zellen",
                               "Belastung durch radioaktive Strahlung",
                               "Test auf Allergie ohne autoaggressive Reaktion (Allergietyp I)",
                               "Test auf Autoimmunreaktion",
                               "Test auf Immunschwäche - Defizite",
                               "Bakterielle Infektion im allgemeinen (spezifischen Erreger testen!)",
                               "Virale Infektion im allgemeinen (spezifischen Erreger testen)",
                               "Test auf Parasiten im allgemeinen",
                               "Test auf Pilzbefall durch Candida albicans",
                               "Reaktion auf Mischung 1",
                               "Reaktion auf Mischung 2",
                               "Veränderung der Blutzusammensetzung",
                               "Belastung der Organismus durch tierische Eiweisse",
                               "Belastung des Organismus durch freie Radikale",
                               "Störung durch gen-manipulierte Lebensmittel",
                               "Verwertungsstörung",
                               "Störungen im Säuren-Basen-Haushalt - Übersäuerung",
                               "Störungen im Säuren-Basen-Haushalt - alkalische Reaktion",
                               "Belastungen des Organismus durch Stoffwechselträgheit",
                               "bzw. Ampulle Cholesterinum - Test auf erhöhten Cholesterinspiegel",
                               "Phosphat-Unveträglichkeit (Hyperaktivität o.ä)",
                               "Nahrungsmittelunverträglichkeit",
                               "Nahrungsmittelallergie",
                               "Belastungen durch Dickdarmdysbiose",
                               "Belastungen durch Dünndarmdysbiose",
                               "Belastungen durch Genußmittel (Kaffee, Alkohol, Kakao, Nikotin)",
                               "Störungen durch Sauerstoffmangel",
                               "Test auf Spurenelementmangel",
                               "Test auf Mineralienmangel",
                               "Test auf Vitaminmangel",
                               "Test auf Aminosäureungleichgewicht",
                               "Test auf Enzymmangel",
                               "Hinweis auf psychische Belastung",
                               "Test auf Stressreaktionen",
                               "Symptome durch psychosomatische Störung",
                               "Belastung durch Erschöpfung",
                               "Blockierungen durch psychische Traumata",
                               "Störungen durch Dysbalance des vegetativen Nervensystems",
                               "Test auf endokrine Belastung",
                               "Test auf Hormonmangel",
                               "Energieblockade",
                               "durch negative Gedanken blockierte Therapie",
                               "Symptome durch depressive Belasstungen",
                               "Symptome durch endogene Depression",
                               "Belastung des Organismus durch Therapieschäden",
                               "Hinweis für benigne Tumore (gutartige Formen)",
                               "Hinweis für Präcancerosen (Tumore im Anfangsstudium)",
                               "Hinweis für Kanzerose (Makro-Ca.)",
                               "Hinweis für Prämalignosen (bösartige Tumore am Beginn)",
                               "Hinweis für Prä-Diabetes mellitus",
                               "Hinweis auf Hypertonie und deren schädigen Einfluß",
                               "Hinweis auf Hypotonie und deren Unterversorgung der Gewebe",
                               "Chronische behandlungsresistente Ekzeme",
                               "Unklare Herz-/Kreislaufbahnbeschwerden",
                               "allgemeine Leberbelastung",
                               "Störungen des Organismus durch Verhärtungen, Sklerose",
                               "Regenerationsstörung",
                               "Energie- und Regulationsdefizit",
                               "Löschampulle - zeigt den 'wahren' Test-Wert",
                               "Zelle und Gewebe",
                               "Blut",
                               "Immunsystem",
                               "Lymphsystem",
                               "Kreislaufsystem",
                               "Herz",
                               "Atemwege",
                               "Niere",
                               "Verdauungsystem",
                               "Leber/Galle",
                               "Stoffwechsel",
                               "Bewegungsapparat",
                               "Nervensystem",
                               "Sehorgan",
                               "Hörorgan/Gleichgewichtsorgan",
                               "Haut/Fell",
                               "Hormonsystem",
                               "Weibliche Geschlechtsorgane",
                               "Männliche Geschlechtsorgane",
                               "Psyche",
                               "Stress",
                               "Zähne"]

    def var(self):
        ###FIRST-GROUP###
        self.check_var1 = tk.IntVar()
        self.check_var2 = tk.IntVar()
        self.check_var3 = tk.IntVar()
        self.check_var4 = tk.IntVar()
        self.check_var5 = tk.IntVar()
        self.check_var6 = tk.IntVar()
        self.check_var7 = tk.IntVar()
        self.check_var8 = tk.IntVar()
        self.check_var9 = tk.IntVar()
        self.check_var10 = tk.IntVar()
        self.check_var11 = tk.IntVar()
        self.check_var12 = tk.IntVar()
        self.check_var13 = tk.IntVar()
        self.check_var14 = tk.IntVar()
        self.check_var15 = tk.IntVar()
        self.check_var16 = tk.IntVar()
        self.check_var17 = tk.IntVar()
        ###SECOND-GROUP###
        self.check_var18 = tk.IntVar()
        self.check_var19 = tk.IntVar()
        self.check_var20 = tk.IntVar()
        self.check_var21 = tk.IntVar()
        self.check_var22 = tk.IntVar()
        self.check_var23 = tk.IntVar()
        self.check_var24 = tk.IntVar()
        self.check_var25 = tk.IntVar()
        self.check_var26 = tk.IntVar()
        self.check_var27 = tk.IntVar()
        self.check_var28 = tk.IntVar()
        ###THIRD-GROUP###
        self.check_var29 = tk.IntVar()
        self.check_var30 = tk.IntVar()
        self.check_var31 = tk.IntVar()
        self.check_var32 = tk.IntVar()
        self.check_var33 = tk.IntVar()
        self.check_var34 = tk.IntVar()
        self.check_var35 = tk.IntVar()
        self.check_var36 = tk.IntVar()
        self.check_var37 = tk.IntVar()
        ###FOURTH-GROUP###
        self.check_var38 = tk.IntVar()
        self.check_var39= tk.IntVar()
        self.check_var40 = tk.IntVar()
        self.check_var41 = tk.IntVar()
        self.check_var42 = tk.IntVar()
        self.check_var43 = tk.IntVar()
        self.check_var44 = tk.IntVar()
        self.check_var45 = tk.IntVar()
        self.check_var46 = tk.IntVar()
        self.check_var47 = tk.IntVar()
        self.check_var48 = tk.IntVar()
        self.check_var49 = tk.IntVar()
        self.check_var50 = tk.IntVar()
        self.check_var51 = tk.IntVar()
        self.check_var52 = tk.IntVar()
        self.check_var53 = tk.IntVar()
        self.check_var54 = tk.IntVar()
        self.check_var55 = tk.IntVar()
        self.check_var56 = tk.IntVar()
        self.check_var57 = tk.IntVar()
        self.check_var58 = tk.IntVar()
        ###FIFTH-GROUP###
        self.check_var59 = tk.IntVar()
        self.check_var60 = tk.IntVar()
        self.check_var61= tk.IntVar()
        self.check_var62= tk.IntVar()
        self.check_var63 = tk.IntVar()
        self.check_var64 = tk.IntVar()
        self.check_var65 = tk.IntVar()
        self.check_var66 = tk.IntVar()
        self.check_var67 = tk.IntVar()
        self.check_var68 = tk.IntVar()
        self.check_var69 = tk.IntVar()
        self.check_var70 = tk.IntVar()
        ###SIXTH-GROUP###
        self.check_var71 = tk.IntVar()
        self.check_var72 = tk.IntVar()
        self.check_var73 = tk.IntVar()
        self.check_var74 = tk.IntVar()
        self.check_var75 = tk.IntVar()
        self.check_var76 = tk.IntVar()
        self.check_var77 = tk.IntVar()
        self.check_var78 = tk.IntVar()
        self.check_var79 = tk.IntVar()
        self.check_var80 = tk.IntVar()
        self.check_var81 = tk.IntVar()
        self.check_var82 = tk.IntVar()
        self.check_var83 = tk.IntVar()
        self.check_var84 = tk.IntVar()
        self.check_var85 = tk.IntVar()
        self.check_var86 = tk.IntVar()
        self.check_var87 = tk.IntVar()
        self.check_var88 = tk.IntVar()
        self.check_var89 = tk.IntVar()
        self.check_var90 = tk.IntVar()
        self.check_var91 = tk.IntVar()
        self.check_var92 = tk.IntVar()
        self.check_var93 = tk.IntVar()
        self.check_var94 = tk.IntVar()
        self.check_var95 = tk.IntVar()
        self.check_var96 = tk.IntVar()
        self.check_var97 = tk.IntVar()
        self.check_var98 = tk.IntVar()
        self.check_var99 = tk.IntVar()
        self.check_var100 = tk.IntVar()
        self.check_var101 = tk.IntVar()
        self.check_var102 = tk.IntVar()
        ###SECOND-GROUP###
        self.check_var103 = tk.IntVar()
        self.check_var104 = tk.IntVar()
        self.check_var105 = tk.IntVar()
        self.check_var106 = tk.IntVar()
        self.check_var107 = tk.IntVar()

        self.check_bx_values = [self.check_var1, self.check_var2 ,self.check_var3,
                                self.check_var4,self.check_var5,self.check_var6,self.check_var7,self.check_var8,
                                self.check_var9,self.check_var10,self.check_var11,self.check_var12,self.check_var13,
                                self.check_var14,self.check_var15,self.check_var16,self.check_var17,self.check_var18 ,
                                self.check_var19,self.check_var20,self.check_var21,self.check_var22,self.check_var23,
                                self.check_var24,self.check_var25,self.check_var26,self.check_var27,self.check_var28,
                                self.check_var29,self.check_var30,self.check_var31,self.check_var32,self.check_var33,
                                self.check_var34,self.check_var35,self.check_var36,self.check_var37,self.check_var38,
                                self.check_var39,self.check_var40,self.check_var41,self.check_var42,self.check_var43,
                                self.check_var44,self.check_var45,self.check_var46,self.check_var47,self.check_var48,
                                self.check_var49,self.check_var50,self.check_var51,self.check_var52,self.check_var53,
                                self.check_var54,self.check_var55,self.check_var56,self.check_var57,self.check_var58,
                                self.check_var59,self.check_var60,self.check_var61,self.check_var62,self.check_var63,
                                self.check_var64,self.check_var65 ,self.check_var66 ,self.check_var67 ,self.check_var68,
                                self.check_var69,self.check_var70 ,self.check_var71 ,self.check_var72 ,self.check_var73,
                                self.check_var74, self.check_var75 ,self.check_var76, self.check_var77 ,self.check_var78,
                                self.check_var79, self.check_var80,self.check_var81,self.check_var82,self.check_var83,
                                self.check_var84,self.check_var85,self.check_var86, self.check_var87, self.check_var88,
                                self.check_var89 ,self.check_var90,self.check_var91, self.check_var92, self.check_var93,
                                self.check_var94, self.check_var95, self.check_var96, self.check_var97,
                                self.check_var98, self.check_var99, self.check_var100,self.check_var101,
                                self.check_var102,self.check_var103,self.check_var104,self.check_var105,
                                self.check_var106,self.check_var107]


    def check_values(self):
        print("Entered function!")
        for i in self.check_bx_values:
            i.set(0)

    def create(self):
        print("Entered create Function!")
        checked = []
        for item in self.check_bx_values:
            print("Value is:", item.get(), "Index is:", self.check_bx_values.index(item))
            if item.get() == 1:
                checked.append(self.check_bx_values.index(item))
        for item in checked:
            self.output.append(self.complete_entries[item])
        if self.dir == "NULL" or self.dir == "":
            simpledialog.messagebox.showerror("Fehler!", "Bitte einen Speicherort angeben.")
            return 0
        file_name = simpledialog.askstring("Dateiname", "Bitte geben Sie einen Dateinamen ein. Hinweis: Beim Verwenden von vorhandenen Dateinamen, führt dies dazu, das die derzeitige Datei nicht gespeichert wird!")
        dir = str(self.dir + "/" + file_name + ".xlsx")
        print(dir)
        workbook = xls.Workbook(dir)
        worksheet = workbook.add_worksheet()
        worksheet.write("A1", "Tiere in Balance")
        worksheet.write("A2", "Susanne Dambowy, THP")
        worksheet.write("A3", "Thomas-Mann-Straße 36")
        worksheet.write("A4", "63486 Bruchköbel - Roßdorf")
        worksheet.write("A6", "Tel. 0151-19180808")
        worksheet.write("A7", "www.pferde-in-balance.eu")
        worksheet.write("A8", "susanne.dambowy@pferde-in-balance.eu")
        worksheet.write("A10", "Analyse vom: ")
        worksheet.write("A11", "Analyse für: ")
        worksheet.write("A13", "Belastung des Gewebes:")
        g1_row = 13
        for i in self.group1_entries:
            worksheet.write(g1_row, 1, i)
            if i in self.output:
                worksheet.write(g1_row, 10, u'\u2713')
            else:
                worksheet.write(g1_row, 10, "X")
            g1_row += 1

        worksheet.write("A34", "Toxische und umweltbedingte Belastungen:")
        g2_row = 34
        for i in self.group2_entries:
            worksheet.write(g2_row, 1, i)
            if i in self.output:
                worksheet.write(g2_row, 10, u'\u2713')
            else:
                worksheet.write(g2_row, 10, "X")
            g2_row += 1

        worksheet.write("A48", "Immunreaktion:")
        g3_row = 48
        for i in self.group3_entries:
            worksheet.write(g3_row, 1, i)
            if i in self.output:
                worksheet.write(g3_row, 10, u'\u2713')
            else:
                worksheet.write(g3_row, 10, "X")
            g3_row += 1

        worksheet.write("A67", "Ernährungsbereich und Stoffwechsel:")
        g4_row = 67
        for i in self.group4_entries:
            worksheet.write(g4_row, 1, i)
            if i in self.output:
                worksheet.write(g4_row, 10, u'\u2713')
            else:
                worksheet.write(g4_row, 10, "X")
            g4_row += 1

        worksheet.write("A90", "Psychische Situation:")
        g5_row = 90
        for i in self.group5_entries:
            worksheet.write(g5_row, 1, i)
            if i in self.output:
                worksheet.write(g5_row, 10, u'\u2713')
            else:
                worksheet.write(g5_row, 10, "X")
            g5_row += 1

        worksheet.write("A104", "diverse pathologische Erscheinungen:")
        g6_row = 104
        for i in self.group6_entries:
            worksheet.write(g6_row, 1, i)
            if i in self.output:
                worksheet.write(g6_row, 10, u'\u2713')
            else:
                worksheet.write(g6_row, 10, "X")
            g6_row += 1

        worksheet.write("A121", "Physiologie Pferd")
        g7_row = 121
        for i in self.group7_entries:
            worksheet.write(g7_row, 1, i)
            if i in self.output:
                worksheet.write(g7_row, 10, u'\u2713')
            else:
                worksheet.write(g7_row, 10, "X")
            g7_row += 1

        worksheet.write("A145", "Futtertest:")
        worksheet.write("A155", "Therapieempfehlung:")

        simpledialog.messagebox.showinfo("Information", "Das Exportieren war erfolgreich!")
        workbook.close()


    def save(self):
        self.dir = filedialog.askdirectory()


    def init_components(self):
        self.title = tk.Label(self.root, text="Testbogen")
        self.menubar = tk.Menu(self.root)
        self.menubar.add_cascade(label="Zurücksetzen", command= lambda: window.check_values())
        self.menubar.add_cascade(label="Exportieren", command= lambda: window.create())
        self.menubar.add_cascade(label="Speicherort", command= lambda: window.save())
        ###FIRST-GROUP###
        self.mb = tk.Menubutton(self.root, text="Belastung des Gewebes", relief=tk.RAISED)
        self.mb.menu  =  tk.Menu ( self.mb, tearoff = 0 )
        self.mb["menu"]  =  self.mb.menu
        self.mb.menu.add_checkbutton ( label=self.group1_entries[0], variable=self.check_var1)
        self.mb.menu.add_checkbutton ( label=self.group1_entries[1], variable=self.check_var2)
        self.mb.menu.add_checkbutton ( label=self.group1_entries[2], variable=self.check_var3)
        self.mb.menu.add_checkbutton ( label=self.group1_entries[3], variable=self.check_var4)
        self.mb.menu.add_checkbutton ( label=self.group1_entries[4], variable=self.check_var5)
        self.mb.menu.add_checkbutton ( label=self.group1_entries[5], variable=self.check_var6)
        self.mb.menu.add_checkbutton ( label=self.group1_entries[6], variable=self.check_var7)
        self.mb.menu.add_checkbutton ( label=self.group1_entries[7], variable=self.check_var8)
        self.mb.menu.add_checkbutton ( label=self.group1_entries[8], variable=self.check_var9)
        self.mb.menu.add_checkbutton ( label=self.group1_entries[9], variable=self.check_var10)
        self.mb.menu.add_checkbutton ( label=self.group1_entries[10], variable=self.check_var11)
        self.mb.menu.add_checkbutton ( label=self.group1_entries[11], variable=self.check_var12)
        self.mb.menu.add_checkbutton ( label=self.group1_entries[12], variable=self.check_var13)
        self.mb.menu.add_checkbutton ( label=self.group1_entries[13], variable=self.check_var14)
        self.mb.menu.add_checkbutton ( label=self.group1_entries[14], variable=self.check_var15)
        self.mb.menu.add_checkbutton ( label=self.group1_entries[15], variable=self.check_var16)
        self.mb.menu.add_checkbutton ( label=self.group1_entries[16], variable=self.check_var17)
        ###SECOND-GROUP###
        self.mb2 = tk.Menubutton(self.root, text="Toxische und umweltbedingte Belastungen", relief=tk.RAISED)
        self.mb2.menu  =  tk.Menu ( self.mb2, tearoff = 0 )
        self.mb2["menu"]  =  self.mb2.menu
        self.mb2.menu.add_checkbutton ( label=self.group2_entries[0], variable=self.check_var18)
        self.mb2.menu.add_checkbutton ( label=self.group2_entries[1], variable=self.check_var19)
        self.mb2.menu.add_checkbutton ( label=self.group2_entries[2], variable=self.check_var20)
        self.mb2.menu.add_checkbutton ( label=self.group2_entries[3], variable=self.check_var21)
        self.mb2.menu.add_checkbutton ( label=self.group2_entries[4], variable=self.check_var22)
        self.mb2.menu.add_checkbutton ( label=self.group2_entries[5], variable=self.check_var23)
        self.mb2.menu.add_checkbutton ( label=self.group2_entries[6], variable=self.check_var24)
        self.mb2.menu.add_checkbutton ( label=self.group2_entries[7], variable=self.check_var25)
        self.mb2.menu.add_checkbutton ( label=self.group2_entries[8], variable=self.check_var26)
        self.mb2.menu.add_checkbutton ( label=self.group2_entries[9], variable=self.check_var27)
        self.mb2.menu.add_checkbutton ( label=self.group2_entries[10], variable=self.check_var28)
        ###THIRD-GROUP###
        self.mb3 = tk.Menubutton(self.root, text="Toxische und umweltbedingte Belastungen", relief=tk.RAISED)
        self.mb3.menu  =  tk.Menu ( self.mb3, tearoff = 0 )
        self.mb3["menu"]  =  self.mb3.menu
        self.mb3.menu.add_checkbutton ( label=self.group3_entries[0], variable=self.check_var29)
        self.mb3.menu.add_checkbutton ( label=self.group3_entries[1], variable=self.check_var30)
        self.mb3.menu.add_checkbutton ( label=self.group3_entries[2], variable=self.check_var31)
        self.mb3.menu.add_checkbutton ( label=self.group3_entries[3], variable=self.check_var32)
        self.mb3.menu.add_checkbutton ( label=self.group3_entries[4], variable=self.check_var33)
        self.mb3.menu.add_checkbutton ( label=self.group3_entries[5], variable=self.check_var34)
        self.mb3.menu.add_checkbutton ( label=self.group3_entries[6], variable=self.check_var35)
        self.mb3.menu.add_checkbutton ( label=self.group3_entries[7], variable=self.check_var36)
        self.mb3.menu.add_checkbutton ( label=self.group3_entries[8], variable=self.check_var37)
        ###FOURTH-GROUP###
        self.mb4 = tk.Menubutton(self.root, text="Ernährungsbereich und Stoffwechsel", relief=tk.RAISED)
        self.mb4.menu  =  tk.Menu ( self.mb4, tearoff = 0 )
        self.mb4["menu"]  =  self.mb4.menu
        self.mb4.menu.add_checkbutton ( label=self.group4_entries[0], variable=self.check_var38)
        self.mb4.menu.add_checkbutton ( label=self.group4_entries[1], variable=self.check_var39)
        self.mb4.menu.add_checkbutton ( label=self.group4_entries[2], variable=self.check_var40)
        self.mb4.menu.add_checkbutton ( label=self.group4_entries[3], variable=self.check_var41)
        self.mb4.menu.add_checkbutton ( label=self.group4_entries[4], variable=self.check_var42)
        self.mb4.menu.add_checkbutton ( label=self.group4_entries[5], variable=self.check_var43)
        self.mb4.menu.add_checkbutton ( label=self.group4_entries[6], variable=self.check_var44)
        self.mb4.menu.add_checkbutton ( label=self.group4_entries[7], variable=self.check_var45)
        self.mb4.menu.add_checkbutton ( label=self.group4_entries[8], variable=self.check_var46)
        self.mb4.menu.add_checkbutton ( label=self.group4_entries[9], variable=self.check_var47)
        self.mb4.menu.add_checkbutton ( label=self.group4_entries[10], variable=self.check_var48)
        self.mb4.menu.add_checkbutton ( label=self.group4_entries[11], variable=self.check_var49)
        self.mb4.menu.add_checkbutton ( label=self.group4_entries[12], variable=self.check_var50)
        self.mb4.menu.add_checkbutton ( label=self.group4_entries[13], variable=self.check_var51)
        self.mb4.menu.add_checkbutton ( label=self.group4_entries[14], variable=self.check_var52)
        self.mb4.menu.add_checkbutton ( label=self.group4_entries[15], variable=self.check_var53)
        self.mb4.menu.add_checkbutton ( label=self.group4_entries[16], variable=self.check_var54)
        self.mb4.menu.add_checkbutton ( label=self.group4_entries[17], variable=self.check_var55)
        self.mb4.menu.add_checkbutton ( label=self.group4_entries[18], variable=self.check_var56)
        self.mb4.menu.add_checkbutton ( label=self.group4_entries[19], variable=self.check_var57)
        self.mb4.menu.add_checkbutton ( label=self.group4_entries[20], variable=self.check_var58)
        ###FIFTH-GROUP###
        self.mb5 = tk.Menubutton(self.root, text="Psychische Situation", relief=tk.RAISED)
        self.mb5.menu  =  tk.Menu ( self.mb5, tearoff = 0 )
        self.mb5["menu"]  =  self.mb5.menu
        self.mb5.menu.add_checkbutton ( label=self.group5_entries[0], variable=self.check_var59)
        self.mb5.menu.add_checkbutton ( label=self.group5_entries[1], variable=self.check_var60)
        self.mb5.menu.add_checkbutton ( label=self.group5_entries[2], variable=self.check_var61)
        self.mb5.menu.add_checkbutton ( label=self.group5_entries[3], variable=self.check_var62)
        self.mb5.menu.add_checkbutton ( label=self.group5_entries[4], variable=self.check_var63)
        self.mb5.menu.add_checkbutton ( label=self.group5_entries[5], variable=self.check_var64)
        self.mb5.menu.add_checkbutton ( label=self.group5_entries[6], variable=self.check_var65)
        self.mb5.menu.add_checkbutton ( label=self.group5_entries[7], variable=self.check_var66)
        self.mb5.menu.add_checkbutton ( label=self.group5_entries[8], variable=self.check_var67)
        self.mb5.menu.add_checkbutton ( label=self.group5_entries[9], variable=self.check_var68)
        self.mb5.menu.add_checkbutton ( label=self.group5_entries[10], variable=self.check_var69)
        self.mb5.menu.add_checkbutton ( label=self.group5_entries[11], variable=self.check_var70)
        ###SIXTH-GROUP###
        self.mb6 = tk.Menubutton(self.root, text="diverse pathologische Erscheinungen", relief=tk.RAISED)
        self.mb6.menu  =  tk.Menu ( self.mb6, tearoff = 0 )
        self.mb6["menu"]  =  self.mb6.menu
        self.mb6.menu.add_checkbutton ( label=self.group6_entries[0], variable=self.check_var71)
        self.mb6.menu.add_checkbutton ( label=self.group6_entries[1], variable=self.check_var72)
        self.mb6.menu.add_checkbutton ( label=self.group6_entries[2], variable=self.check_var73)
        self.mb6.menu.add_checkbutton ( label=self.group6_entries[3], variable=self.check_var74)
        self.mb6.menu.add_checkbutton ( label=self.group6_entries[4], variable=self.check_var75)
        self.mb6.menu.add_checkbutton ( label=self.group6_entries[5], variable=self.check_var76)
        self.mb6.menu.add_checkbutton ( label=self.group6_entries[6], variable=self.check_var77)
        self.mb6.menu.add_checkbutton ( label=self.group6_entries[7], variable=self.check_var78)
        self.mb6.menu.add_checkbutton ( label=self.group6_entries[8], variable=self.check_var79)
        self.mb6.menu.add_checkbutton ( label=self.group6_entries[9], variable=self.check_var80)
        self.mb6.menu.add_checkbutton ( label=self.group6_entries[10], variable=self.check_var81)
        self.mb6.menu.add_checkbutton ( label=self.group6_entries[11], variable=self.check_var82)
        self.mb6.menu.add_checkbutton ( label=self.group6_entries[12], variable=self.check_var83)
        self.mb6.menu.add_checkbutton ( label=self.group6_entries[13], variable=self.check_var84)
        self.mb6.menu.add_checkbutton ( label=self.group6_entries[14], variable=self.check_var85)
        ###SEVENTH-GROUP###
        self.mb7 = tk.Menubutton(self.root, text="Physiologie Pferd", relief=tk.RAISED)
        self.mb7.menu  =  tk.Menu ( self.mb7, tearoff = 0 )
        self.mb7["menu"]  =  self.mb7.menu
        self.mb7.menu.add_checkbutton ( label=self.group7_entries[0], variable=self.check_var86)
        self.mb7.menu.add_checkbutton ( label=self.group7_entries[1], variable=self.check_var87)
        self.mb7.menu.add_checkbutton ( label=self.group7_entries[2], variable=self.check_var88)
        self.mb7.menu.add_checkbutton ( label=self.group7_entries[3], variable=self.check_var89)
        self.mb7.menu.add_checkbutton ( label=self.group7_entries[4], variable=self.check_var90)
        self.mb7.menu.add_checkbutton ( label=self.group7_entries[5], variable=self.check_var91)
        self.mb7.menu.add_checkbutton ( label=self.group7_entries[6], variable=self.check_var92)
        self.mb7.menu.add_checkbutton ( label=self.group7_entries[7], variable=self.check_var93)
        self.mb7.menu.add_checkbutton ( label=self.group7_entries[8], variable=self.check_var94)
        self.mb7.menu.add_checkbutton ( label=self.group7_entries[9], variable=self.check_var95)
        self.mb7.menu.add_checkbutton ( label=self.group7_entries[10], variable=self.check_var96)
        self.mb7.menu.add_checkbutton ( label=self.group7_entries[11], variable=self.check_var97)
        self.mb7.menu.add_checkbutton ( label=self.group7_entries[12], variable=self.check_var98)
        self.mb7.menu.add_checkbutton ( label=self.group7_entries[13], variable=self.check_var99)
        self.mb7.menu.add_checkbutton ( label=self.group7_entries[14], variable=self.check_var100)
        self.mb7.menu.add_checkbutton ( label=self.group7_entries[15], variable=self.check_var101)
        self.mb7.menu.add_checkbutton ( label=self.group7_entries[16], variable=self.check_var102)
        self.mb7.menu.add_checkbutton ( label=self.group7_entries[17], variable=self.check_var103)
        self.mb7.menu.add_checkbutton ( label=self.group7_entries[18], variable=self.check_var104)
        self.mb7.menu.add_checkbutton ( label=self.group7_entries[19], variable=self.check_var104)
        self.mb7.menu.add_checkbutton ( label=self.group7_entries[20], variable=self.check_var105)
        self.mb7.menu.add_checkbutton ( label=self.group7_entries[21], variable=self.check_var106)

    def configure_components(self):
        self.title.configure(font=("Helvetica","20","bold"))
        self.root.config(menu = self.menubar)


    def place_components(self):
        self.title.grid(row=0, column=2)
        self.mb.grid(row=1, column=1, sticky = "NSEW")
        self.mb2.grid(row=1, column=2, sticky = "NSEW")
        self.mb3.grid(row=1, column=3, sticky = "NSEW")
        self.mb4.grid(row=2, column=1, sticky = "NSEW")
        self.mb5.grid(row=2, column=2, sticky = "NSEW")
        self.mb6.grid(row=2, column=3, sticky = "NSEW")
        self.mb7.grid(row=3, column=2, sticky = "NSEW")


window = Window()
window.var()
window.init_components()
window.configure_components()
window.place_components()
window.root.mainloop()
