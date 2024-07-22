#Text                   Background                   Style

#30------grey           cinza------40                0-text normal
#31------red            vermelho------41             1-negrito   
#32------green          verde------42                4-sublinhado
#33------yellow         amarelo------43              7-inverso
#34------roxo           purple------44 
#35------pink           rosa------45  
#36------cyan           ciano------46  
#37------white          branco------107

#padrao \033[x;x;xm
print('\033[31;42mOlá Mundo!\33[m')
print('\033[4;37;45mOlá Mundo!\33[m')
print('\033[1;33;44mOlá Mundo!\33[m')
print('\033[7;33;44mOlá Mundo!\33[m')
