from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Custom monosaccharide generator - Mark Mazurek')

# Relief variable
relief_type = RAISED
menu_background_colour = 'light grey'
highlightbackground_colour = 'light grey'
highlightthickness_value = 0
bg_inputtxt = 'white'
bg_outputtxt = 'white'

# Frame dimensions
column_0_width = 800
column_1_width = 250
row_0_height = 550
row_1_height = 28
row_2_height = 155
Font_tuple = ("Calibri Light", 12, 'bold')
Font_tuple2 = ("Calibri Light", 35, 'bold')
Font_tuple3 = ("Calibri Light", 16, 'bold')
sub_entry_width = 15
button_width = 15

SHORT_FORM_IDENTITIES = {
    'Ac' : 'acetyl',
    'All' : 'allyl',
    'Bn' : 'benzyl',
    'Br' : 'bromine',
    'Bu' : 'butyl',
    'Bz' : 'benzoyl',
    'Cbz' : 'benzyloxycarbonyl',
    'CDA' : 'cyclohexane-1,2-diacetal',
    'Cl' : 'chloro',
    'ClAc' : 'chloroacetyl',
    'DCA' : '?',
    'DMT' : 'dimethoxytrityl',
    'Et' : 'ethyl',
    'F' : 'fluoro',
    'Hex' : 'hexyl',
    'I' : 'iodo',
    'iBu' : 'isobutyl',
    'iPent' : 'isopentyl',
    'iPr' : 'isopropyl',
    'Lev' : 'levulinoyl',
    'Me' : 'methyl',
    'Ms' : 'mesyl',
    'N3' : 'azido',
    'opNDP' : '2,4-dinitrophenyl',
    'Pent' : 'pentyl',
    'Ph' : 'phenyl',
    'Phth' : 'phthalimidoyl',
    'Pic' : 'picolyl',
    'Piv' : 'pivaloyl',
    #'pMOPh' : ['paramethoxyphenyl', '4-methoxyphenyl', 'PMP'],
    'PMB' : 'paramethoxybenzyl',
    'PNP' : 'paranitrophenyl',
    'PPG' : 'propargyl',
    'Pr' : 'propyl',
    'sBu' : 'sec-butyl',
    'sHex' : 'sec-hexyl',
    'sPent' : 'sec-pentyl',
    'TBDPS' : 'tert-butyldiphenylsilyl',
    'TBS' : 'tert-butyldimethylsilyl',
    'TES' : 'triethylsilyl',
    'TCA' : 'trichloroacetyl',
    'TCAI' : 'trichloroacetimidoyl',
    'Tf' : 'triflyl',
    'Trt' : 'trityl',
    #'Ts' : ['tosyl', 'toluenesulfonyl'],
}

# Dictionary of aldohexoses
aldohexoses_definition = {
    '0000' : ('D-all'),
    '0001' : ('D-altr'), 
    '0010' : ('D-gluc'), 
    '0011' : ('D-mann'),
    '0100' : ('D-gul'),
    '0101' : ('D-id'), 
    '0110' : ('D-gal'), 
    '0111' : ('D-tal'),
    '1111' : ('L-all'),
    '1110' : ('L-altr'),
    '1101' : ('L-gluc'), 
    '1001' : ('L-mann'),
    '1011' : ('L-gul'),
    '1010' : ('L-id'),
    '1001' : ('L-gal'),
    '1000' : ('L-tal')}

 # Duplicator dictionary
dup_definition = {
    '1': '',
    '2':'di-',
    '3': 'tri-',
    '4': 'tetra-',
    '5': 'penta-',
    '6': 'hexa-',
    '7': 'hepta-',
    '8': 'octa-',
    '9': 'nona-',
    '10': 'deca-',
    '11': 'undeca-',
    '12': 'dodeca-',}
           
def callback():
    # Delete previous output textbox contents
    name_output.delete(1.0,END)
    description_output.delete(1.0,END)
    qpt_output.delete(1.0,END)

    #callback Substituents
    sub1 = entry.get()
    sub2 = entry2.get()
    sub3 = entry3.get()
    sub4 = entry4.get()
    sub5 = entry5.get()
    sub6 = entry6.get()

    #callback Deoxy
    if deoxy1.get() == 1:
        print('Deoxy at C(1)')

    else:
        pass

    if deoxy2.get() == 1:
        print('Deoxy at C(2)')
    else:
        pass

    if deoxy3.get() == 1:
        print('Deoxy at C(3)')
    else:
        pass

    if deoxy4.get() == 1:
        print('Deoxy at C(4)')
    else:
        pass

    if deoxy5.get() == 1:
        print('Deoxy at C(5)')
    else:
        pass

    if deoxy6.get() == 1:
        print('Deoxy at C(6)')
    else:
        pass


 # callback String creator
    print('Substituent list of entered compound for name generation and look up:')
    sugar_identifier = ([ori1.get(), ori2.get(), ori3.get(), ori4.get(), ori5.get(), 0,
        sub1, sub2, sub3, sub4, sub5, sub6, 
        deoxy1.get(), deoxy2.get(), deoxy3.get(), deoxy4.get(), deoxy5.get(), deoxy6.get()])
    sugar_identifier_condensed = [(str(ori1.get()) + (str(ori2.get()) + str(ori3.get()) + str(ori4.get()) + str(ori5.get()) + '0'),
        sub1, sub2, sub3, sub4, sub5, sub6, 
        str(deoxy1.get()) + str(deoxy2.get()) + str(deoxy3.get()) + str(deoxy4.get()) + str(deoxy5.get()) + str(deoxy6.get()))]
    
    print(sugar_identifier)
    print(sugar_identifier_condensed)

    def sugar_stringer():
        print('C dictionary: ')
        c_dictionary = {}
        for number in range(1,7):
            c_dictionary["C%s" %number] = ['%s' %number, '0', '', '0']
        c_dictionary['C1'][2] = sub1
        c_dictionary['C2'][2] = sub2
        c_dictionary['C3'][2] = sub3
        c_dictionary['C4'][2] = sub4
        c_dictionary['C5'][2] = sub5
        c_dictionary['C6'][2] = sub6

        [print(key,':',value) for key, value in c_dictionary.items()]


        sub_list = [sub1, sub2, sub3, sub4, sub5, sub6]
        binary_sugar_identity = (str(sugar_identifier[4]) + 
                                 str(sugar_identifier[3]) +
                                 str(sugar_identifier[2]) + 
                                 str(sugar_identifier[1]))
        print('Sugar identity in binary: ' + binary_sugar_identity)
        print(str('Sugar in binary: ' + binary_sugar_identity))
        sugar_identity = aldohexoses_definition.get(binary_sugar_identity)
        default_anomer = 'α/β-'

        if ori1.get() == 1:
            default_anomer = 'β-'
        elif ori1.get() == 0:
            default_anomer = 'α-'

        default_suffix = 'opyranose'

        if sub1 != '':
            default_suffix = 'opyranoside'
        
        sugar_name = (str(default_anomer + sugar_identity + default_suffix))
        print('\n')
        print(str('Sugar name: ' + sugar_name))
        print('\n')
        print('Sub list: ')
        print(sub_list)
        print('\n')
        print('Sub list minus blanks')
        sub_list_minus_blanks = [string for string in sub_list if string != ""]
        print(sub_list_minus_blanks)
        print('\n')
        print('Sub set: ')
        sub_set = set(sub_list_minus_blanks)
        print(sub_set)
        sorted_list_of_sub_set = list(sub_set)
        sorted_list_of_sub_set.sort(key=lambda x: x.strip('()0123456789-'))
        print('Sorted list of sub set:')
        print(sorted_list_of_sub_set)

        # Need a for loop to create below loop and variable 
        # function for each sub.

        combined_list = []

        # For each entry in sorted list of sub set
        for j in sorted_list_of_sub_set:
            # Create indices variable for each sub set entry
            indices = []
            string_duplicator = ''
            string_to_add = ''

            # Loop through sub list 
            for i in range(len(sub_list)):
                if sub_list[i] == j:
                    indices.append(i+1)
            
            # Duplicator adder
            if len(indices) > 0:
                #Duplicator declaration. '2'
                duplicator = str(len(indices))
                print(duplicator)
                #[2,4,]
                string_indices = str(indices)
                #'[2,4,]'
                final_comma_removed = string_indices[:-1]
                string_duplicator = str(dup_definition[duplicator])
                concatenated_num_dup_sub_string = final_comma_removed + '-' + string_duplicator
                final_comma_removed.join((str(string_duplicator) + '-'))
                string_to_add = concatenated_num_dup_sub_string
            stringed_entry = string_to_add + 'O-' + j

            combined_list.append(stringed_entry)
            print(combined_list)
        
        joined_combined_list = '-'.join(combined_list)
        print(joined_combined_list)
        replaced_string = joined_combined_list.replace('[','')
        replaced_string2 = replaced_string.replace(']','')
        replaced_string3 = replaced_string2.replace(' ','')
        replaced_string4 = replaced_string3.replace("'", '')
        print(replaced_string4)

        joined_string_list = replaced_string4 + '-' + str(sugar_name)
        print(joined_string_list)

        name_output.insert(END, (joined_string_list + '\n'))

        name_output.configure(font = Font_tuple3)

        description_output.insert(END, str(sugar_identifier_condensed) + '\n' + '\n' +
            'CAS Number: 142130-42-5' + '\n' +
            'Molecular Formula: C21H24Cl3NO9' + '\n' +
            'Molecular Weight: 540.78g/mol' + '\n' +
            'Chemical Purity: Min. 97% [1H-NMR]' + '\n' +
            'Appearance: Colourless syrup' + '\n' +
            'Solubility: DMSO, DMF, DCM, EtOAc')

        description_output.configure(font = Font_tuple)

        qpt_output.insert(END, 'Quantity                Price                       Time' + '\n' + '\n' +
            '250mg              $130.00                In stock' + '\n' +
            '500mg             $210.00                In stock' + '\n' +
            '1g                      $360.00                In stock' + '\n' +
            '2g                      $660.00                3 weeks')

        qpt_output.configure(font = Font_tuple)
        


    sugar_stringer()

# 

# Frame 1 Visual display/input frame
frame1 = Frame(root, width=column_0_width, height=row_0_height, bg='white', bd='5', highlightbackground = highlightbackground_colour, highlightthickness = highlightthickness_value)
frame1.grid(row=0, column=0, sticky='NESW')
frame1.grid_propagate(0)


#Visual input canvas
canvas_height = 550
canvas_width = 800
x = 40
y = -50

hex_superwest = 30 + x
hex_west = 150 + x
hex_centerwest = 270 + x
hex_center = 400 + x
hex_centereast = 530 + x
hex_east = 650 + x

hex_top = 105 + y
hex_shoulder = 185 + y
hex_hip = 325 + y
hex_knee = 410 + y
hex_foot = 545 + y

textbox_width = 85


main_canvas = Canvas(frame1, width=canvas_width, height=canvas_height)

main_canvas.create_polygon(hex_center,hex_top, hex_centereast,hex_shoulder, hex_centereast,hex_hip, 
                         hex_center,hex_knee, hex_centerwest,hex_hip, hex_centerwest,hex_shoulder, 
                         outline='black', fill='white', width = 5)
main_canvas.create_line(hex_west,hex_top, hex_centerwest,hex_shoulder, width=5)
main_canvas.create_line(hex_west,hex_knee, hex_centerwest,hex_hip, width=5)
main_canvas.create_line(hex_center,hex_knee, hex_center,hex_foot, width=5)
main_canvas.create_line(hex_centereast,hex_hip, hex_east,hex_knee, width=5)
main_canvas.create_line(hex_centereast,hex_shoulder, hex_east,hex_top, width=5)
main_canvas.create_line(hex_west,hex_top, hex_superwest,hex_shoulder, width=5)
entry1 = ttk.Entry(root)
entry2 = ttk.Entry(root) 
entry3 = ttk.Entry(root) 
entry4 = ttk.Entry(root) 
entry6 = ttk.Entry(root)

main_canvas.create_window(hex_east, hex_top, window=entry1, width=textbox_width)
main_canvas.create_window(hex_east, hex_knee, window=entry2, width=textbox_width)
main_canvas.create_window(hex_center, hex_foot, window=entry3, width=textbox_width)
main_canvas.create_window(hex_west, hex_knee, window=entry4, width=textbox_width)
main_canvas.create_window(hex_superwest, hex_shoulder, window=entry6, width=textbox_width)

entry1.insert(0, 'OH')
entry1.configure(font = Font_tuple2)
entry2.insert(0, 'OH')
entry2.configure(font = Font_tuple2)
entry3.insert(0, 'OH')
entry3.configure(font = Font_tuple2)
entry4.insert(0, 'HO')
entry4.configure(font = Font_tuple2)
entry6.insert(0, 'HO')
entry6.configure(font = Font_tuple2)

#Packing main canvas into frame1
main_canvas.grid(row=0,column=0, sticky = 'N')


# Frame 2 Orientations/Substituents/Deoxy frame
frame2 = Frame(root, width=column_1_width, height=row_0_height, bg='white', bd='0', highlightbackground = highlightbackground_colour, highlightthickness = highlightthickness_value)
frame2.grid(row=0, column=1, sticky='NESW')
frame2.grid_propagate(0)

label200 = Label(frame2, text='Ori', font = Font_tuple)
label200.grid(row=0,column=1)
label201 = Label(frame2, text='Substituent', font = Font_tuple)
label201.grid(row=0,column=2)
label202 = Label(frame2, text='Deo', font = Font_tuple)
label202.grid(row=0,column=3)

label20 = Label(frame2, text='C(1)', font = Font_tuple)
label20.grid(row=1,column=0)
label21 = Label(frame2, text='C(2)', font = Font_tuple)
label21.grid(row=2,column=0)
label22 = Label(frame2, text='C(3)', font = Font_tuple)
label22.grid(row=3,column=0)
label23 = Label(frame2, text='C(4)', font = Font_tuple)
label23.grid(row=4,column=0)
label24 = Label(frame2, text='C(5)', font = Font_tuple)
label24.grid(row=5,column=0)
label25 = Label(frame2, text='C(6)', font = Font_tuple)
label25.grid(row=6,column=0)


# Input for orientation of hydroxyl groups
ori1 = IntVar()
ori1.set(1)
cbox_ori1 = Checkbutton(frame2, variable=ori1, command=callback).grid(row=1, column=1)

ori2 = IntVar()
ori2.set(0)
cbox_ori2 = Checkbutton(frame2, variable=ori2, command=callback).grid(row=2, column=1)

ori3 = IntVar()
ori3.set(1)
cbox_ori3 = Checkbutton(frame2, variable=ori3, command=callback).grid(row=3, column=1)

ori4 = IntVar()
ori4.set(0)
cbox_ori4 = Checkbutton(frame2, variable=ori4, command=callback).grid(row=4, column=1)

ori5 = IntVar()
ori5.set(0)
cbox_ori5 = Checkbutton(frame2, variable=ori5, command=callback).grid(row=5, column=1)

#Substituents
entry = ttk.Entry(frame2, width = sub_entry_width)
entry.grid(row=1,column=2)
entry2 = ttk.Entry(frame2, width = sub_entry_width)
entry2.grid(row=2,column=2)
entry3 = ttk.Entry(frame2, width = sub_entry_width)
entry3.grid(row=3,column=2)
entry4 = ttk.Entry(frame2, width = sub_entry_width)
entry4.grid(row=4,column=2)
entry5 = ttk.Entry(frame2, width = sub_entry_width)
entry5.grid(row=5,column=2)
entry6 = ttk.Entry(frame2, width = sub_entry_width)
entry6.grid(row=6,column=2)

entry.insert(0, 'trichloroacetimidoyl')
entry2.insert(0, 'acetyl')
entry3.insert(0, 'benzyl')
entry4.insert(0, 'acetyl')
entry5.insert(0, '')
entry6.insert(0, 'acetyl')

# Input for deoxygenated carbons
deoxy1 = IntVar()
deoxy1.set(0)
cbox_deoxy1 = Checkbutton(frame2, variable=deoxy1).grid(row=1, column=3)

deoxy2 = IntVar()
deoxy2.set(0)
cbox_deoxy2 = Checkbutton(frame2, variable=deoxy2).grid(row=2, column=3)

deoxy3 = IntVar()
deoxy3.set(0)
cbox_deoxy3 = Checkbutton(frame2, variable=deoxy3).grid(row=3, column=3)

deoxy4 = IntVar()
deoxy4.set(0)
cbox_deoxy4 = Checkbutton(frame2, variable=deoxy4).grid(row=4, column=3)

deoxy5 = IntVar()
deoxy5.set(0)
cbox_deoxy5 = Checkbutton(frame2, variable=deoxy5).grid(row=5, column=3)

deoxy6 = IntVar()
deoxy6.set(0)
cbox_deoxy6 = Checkbutton(frame2, variable=deoxy6).grid(row=6, column=3)

label_blank = Label(frame2, text='')
label_blank.grid(row=8,column=1)

# Generate button
button1 = ttk.Button(frame2, text = 'Update substituents', command = callback, width = button_width)
button1.grid(row=9, column=1, columnspan = 3, sticky = 'E')

# Other buttons
button2 = ttk.Button(frame2, text = 'Order', command = callback, width = button_width)
button2.grid(row=11, column=1, columnspan = 3, sticky = 'E')
button3 = ttk.Button(frame2, text = 'Request quote', command = callback, width = button_width)
button3.grid(row=12, column=1, columnspan = 3, sticky = 'E')
button4 = ttk.Button(frame2, text = 'Reset to glucose', command = callback, width = button_width)
button4.grid(row=14, column=1, columnspan = 3, sticky = 'E')
button5 = ttk.Button(frame2, text = 'Save structure', command = callback, width = button_width)
button5.grid(row=15, column=1, columnspan = 3, sticky = 'E')
button6 = ttk.Button(frame2, text = 'Physical properties', command = callback, width = button_width)
button6.grid(row=16, column=1, columnspan = 3, sticky = 'E')
button7 = ttk.Button(frame2, text = 'Change projection', command = callback, width = button_width)
button7.grid(row=17, column=1, columnspan = 3, sticky = 'E')

# Frame 3 Generated string display frame
frame3 = Frame(root, width=column_0_width, height=row_1_height, bg=menu_background_colour, bd='0', highlightbackground = highlightbackground_colour, highlightthickness = highlightthickness_value)
frame3.grid(row=1, column=0, columnspan = 2, sticky='NESW')
frame3.grid_propagate(0)
name_output = Text(frame3, height = 1, width = 119, bg = bg_outputtxt)
name_output.grid(row=0,column=0)

# Frame 5 Product description
frame5 = Frame(root, width=column_0_width, height=row_2_height, bg=menu_background_colour, bd='0', highlightbackground = highlightbackground_colour, highlightthickness = highlightthickness_value)
frame5.grid(row=2, column=0, sticky='NESW')
frame5.grid_propagate(0)
label5 = Label(frame5, text='Description and physical properties:', font = Font_tuple, bg='beige')
label5.grid(row=0,column=0, sticky = 'W')
description_output = Text(frame5, height = 11, width = 84, bg = 'beige', font = Font_tuple)
description_output.grid(row=1,column=0)

# Frame 6 Q/P/T
frame6 = Frame(root, width=column_1_width, height=row_2_height, bg=menu_background_colour, bd='0', highlightbackground = highlightbackground_colour, highlightthickness = highlightthickness_value)
frame6.grid(row=2, column=1, sticky='NESW')
frame6.grid_propagate(0)
label6 = Label(frame6, text='Order info:', font = Font_tuple, bg = 'beige')
label6.grid(row=0,column=0, sticky = 'W')
qpt_output = Text(frame6, height = 11, width = 34, font = Font_tuple, bg = 'beige')
qpt_output.grid(row=2,column=0)

callback()

root.geometry()

root.mainloop()
