xlsx2csv P*.xlsx > pozos.csv 	# Convertir a CSV.
sed -i '1,8d' pozos.csv		# Eliminar las primeras ocho líneas.
sed -i "s/  */ /g" pozos.csv	# Borrar dobles espacios.
