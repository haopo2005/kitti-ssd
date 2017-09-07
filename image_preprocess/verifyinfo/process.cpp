#include "opencv2/objdetect.hpp"
#include "opencv2/videoio.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"
#include <fstream>
#include <iostream>
#include <stdio.h>

using namespace std;
using namespace cv;


int main( int argc, char *argv[] )
{
	FILE *fp;
	float x,y,w,h;
	fp = fopen(argv[1],"r");
	cv::Mat src=cv::imread(argv[2],1);
	while(1)
	{
		fscanf(fp,"%f %f %f %f",&x, &y, &w, &h);
		if (feof(fp)) break;
		cv::rectangle(src,cv::Rect(x,y,w,h),cv::Scalar(0,0,255),1,1,0);
	} 
	cv::imwrite(argv[3],src);
    return 0;
}