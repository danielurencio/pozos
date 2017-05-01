xlsx2csv P*.xlsx > pozos.csv 	# Convertir a CSV.
sed -i '1,8d' pozos.csv		# Eliminar las primeras ocho líneas.
sed -i "s/  */ /g" pozos.csv	# Borrar dobles espacios.
sed -i "s/Á/A/g" pozos.csv
sed -i "s/á/a/g" pozos.csv
sed -i "s/É/E/g" pozos.csv
sed -i "s/é/e/g" pozos.csv
sed -i "s/Í/I/g" pozos.csv
sed -i "s/í/i/g" pozos.csv
sed -i "s/Ó/O/g" pozos.csv
sed -i "s/ó/o/g" pozos.csv
sed -i "s/Ú/U/g" pozos.csv
sed -i "s/Ñ/N/g" pozos.csv
sed -i "s/ñ/n/g" pozos.csv
