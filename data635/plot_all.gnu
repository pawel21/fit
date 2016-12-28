set terminal qt size 1820,980 enhanced font 'Verdana,10' persist
set size 1, 1;
set grid;
set key inside center top;
set xlabel "Prąd [A]";
set ylabel "Moc wyjściowa [W]";
set yrange [0<*:]
plot "data_635nm_10_od_razu.txt" using 1:3 title "283 K"
replot "data_635nm_20_od_razu.txt" using 1:3 title "293 K"
replot "data_635nm_30_od_razu.txt" using 1:3 title "303 K"
replot "data_635nm_40_od_razu.txt" using 1:3 title "313 K"
replot "data_635nm_50_od_razu.txt" using 1:3 title "323 K"
