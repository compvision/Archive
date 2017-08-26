#include <opencv2/opencv.hpp>
#include "VideoDevice.hpp"

using namespace cv;

VideoDevice::VideoDevice(){

}

void VideoDevice::initiate(int id){
	camera = VideoCapture(id);
}

Mat VideoDevice::takeImage(){
	camera >> image;
	return image;
}
