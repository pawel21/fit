void plot()
{
	//TNtuple data10("data10", "data10", "J:V:L");
	//data10.ReadFile("data_635nm_10_od_razu.txt");
	//data10.Draw("J:V");
	ifstream in_file;
	in_file.open("data_635nm_10_od_razu.txt");
	double x, y, z;
	while(1) {
	in_file >> x >> y >> z;
	if (!in_file.good()) break;
	printf("%f ", x);
	}	

	//TGraph f("data_635nm_10_od_razu.txt", "%*lg %*lg", " ");
	//f.Draw();
	printf("Hello \n");	
}
