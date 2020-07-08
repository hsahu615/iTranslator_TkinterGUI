from googletrans import Translator
from tkinter import *


def translate():
    translator = Translator()
    a = translator.translate(text.get(), src=clicked.get(), dest=clicked1.get())
    r = a.text
    Result.set(r)


win = Tk()
win.geometry('400x200')
win.title("Sahu's Translator")
win.iconbitmap('icon.ico')

clicked = StringVar()
clicked1 = StringVar()
Result = StringVar()
text = StringVar()

clicked.set('Auto')
label1 = Label(win, text='From:')
label1.grid(row=0, column=0)

OM1 = OptionMenu(win, clicked, 'Auto', 'Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Azerbaijani',
                 'Basque', 'Belarusian', 'Bengali', 'Bosnian', 'Bulgarian', 'Burmese', 'Catalan', 'Cebuano', 'Chewa',
                 'Chinese (Simplified)', 'Chinese (Traditional)''Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch',
                 'English', 'Esperanto', 'Estonian', 'Filipino', 'Finnish', 'French', 'Galician', 'Georgian', 'German',
                 'Greek', 'Gujarati', 'Haitian Creole', 'Hausa', 'Hawaiian', 'Hebrew', 'Hindi', 'Hmong', 'Hungarian',
                 'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kannada', 'Kazakh',
                 'Khmer', 'Kinyarwanda', 'Korean', 'Kurdish (Kurmanji)', 'Kyrgyz', 'Lao', 'Latin', 'Latvian',
                 'Lithuanian', 'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Maori',
                 'Marathi', 'Mongolian', 'Nepali', 'Norwegian (Bokmål)', 'Odia', 'Pashto', 'Persian', 'Polish',
                 'Portuguese', 'Punjabi (Gurmukhi)', 'Romanian', 'Russian', 'Samoan', 'Scots Gaelic', 'Serbian',
                 'Sesotho', 'Shona', 'Sindhi', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese',
                 'Swahili', 'Swedish', 'Tajik', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Turkish', 'Turkmen', 'Ukrainian',
                 'Urdu', 'Uyghur', 'Uzbek', 'Vietnamese', 'Welsh', 'West Frisian', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu')
OM1.grid(row=0, column=1)

clicked1.set('Hindi')

label2 = Label(win, text='To:')
label2.grid(row=0, column=2)

OM2 = OptionMenu(win, clicked1, 'Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Azerbaijani', 'Basque',
                 'Belarusian', 'Bengali', 'Bosnian', 'Bulgarian', 'Burmese', 'Catalan', 'Cebuano', 'Chewa',
                 'Chinese (Simplified)', 'Chinese (Traditional)''Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch',
                 'English', 'Esperanto', 'Estonian', 'Filipino', 'Finnish', 'French', 'Galician', 'Georgian', 'German',
                 'Greek', 'Gujarati', 'Haitian Creole', 'Hausa', 'Hawaiian', 'Hebrew', 'Hindi', 'Hmong', 'Hungarian',
                 'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kannada', 'Kazakh',
                 'Khmer', 'Kinyarwanda', 'Korean', 'Kurdish (Kurmanji)', 'Kyrgyz', 'Lao', 'Latin', 'Latvian',
                 'Lithuanian', 'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Maori',
                 'Marathi', 'Mongolian', 'Nepali', 'Norwegian (Bokmål)', 'Odia', 'Pashto', 'Persian', 'Polish',
                 'Portuguese', 'Punjabi (Gurmukhi)', 'Romanian', 'Russian', 'Samoan', 'Scots Gaelic', 'Serbian',
                 'Sesotho', 'Shona', 'Sindhi', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese',
                 'Swahili', 'Swedish', 'Tajik', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Turkish', 'Turkmen', 'Ukrainian',
                 'Urdu', 'Uyghur', 'Uzbek', 'Vietnamese', 'Welsh', 'West Frisian', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu')
OM2.grid(row=0, column=3)

label3 = Label(win, text='Enter Text: ')
label3.grid(row=1, column=0)

text = StringVar()

entry1 = Entry(win, textvariable=text, bd='5', font=5)
entry1.grid(row=1, column=1)

label4 = Label(win, text='Result: ')
label4.grid(row=2, column=0)

entry2 = Entry(win, textvariable=Result, bd='5', font=5)
entry2.grid(row=2, column=1)

button1 = Button(win, text='Search', command=translate)
button1.grid(row=3, column=0)

button2 = Button(win, text='QUIT', command=win.destroy)
button2.grid(row=3, column=1)

win.mainloop()
