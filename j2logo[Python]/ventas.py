# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	d1 = int()
	d2 = int()
	d3 = int()
	d4 = int()
	d5 = int()
	venta_total = int()
	venta_pro = int()
	pro_1tred = int()
	vent_p_u = int()
	print("Digite las ventas del primer dia")
	d1 = int(input())
	print("Digite las ventas del segundo dia")
	d2 = int(input())
	print("Digite las ventas del tercer dia")
	d3 = int(input())
	print("Digite las ventas del cuarto dia")
	d4 = int(input())
	print("Digite las ventas del quinto dia")
	d5 = int(input())
	venta_total = d1+d2+d3+d4+d5
	venta_pro = (d1+d2+d3+d4+d5)/5
	vent_p_u = d1+d5
	pro_1tred = (d1+d2+d3)/3
	print("La venta total de los cinco dias es:",venta_total)
	print("LA Venta promedio de los cinco dias es:",venta_pro)
	print("La venta total del primer y ultimo dia es:",vent_p_u)
	print("El promedio de los primeros tres dias:",pro_1tred)

