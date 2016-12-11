set terminal qt size 1820,980 enhanced font 'Verdana,10' persist
set size 1, 1;
set grid;
set key inside center top;
set xlabel "Prąd [A]";
set ylabel "Moc wyjściowa [W]";
set yrange [0<*:]
plot "temp_10.txt" using 1:3 title "283 K";
replot "temp_20.txt" using 1:3 title "293 K";
replot "temp_30.txt" using 1:3 title "303 K";
replot "temp_40.txt" using 1:3 title "313 K";
replot "temp_30.txt" using 1:3 title "303 K";
replot "temp_40.txt" using 1:3 title "313 K";
replot "temp_50.txt" using 1:3 title "323 K";
replot "temp_60.txt" using 1:3 title "333 K";
replot "temp_70.txt" using 1:3 title "343 K";
replot "temp_80.txt" using 1:3 title "353 K";
replot "temp_90.txt" using 1:3 title "363 K";
