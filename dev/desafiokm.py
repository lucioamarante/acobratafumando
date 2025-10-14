#digite a area de desmatamento
#area desmatada
#equivalente a XXXX campos de fuebol (arredondando) - use a funcao round



#onversor_desmatamento


area_do_campodefutebol = 6000
m2_m2 = 1000000
area_desmatada=float(input ("digite a area desmatada: "))
area_desmatada= area_desmatada * m2_m2
campos_exatos = area_desmatada/area_do_campodefutebol
print(area_desmatada) 
print(area_do_campodefutebol) 
print(f'{campos_exatos:,.2f}')
