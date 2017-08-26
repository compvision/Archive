#ifndef VIDEO_DEVICE_H
#define VIDEO_DEVICE_H
#include <opencv2/opencv.hpp>

using namespace cv;

class VideoDevice{
	public:
		VideoDevice();
		void initiate(int id);
		Mat takeImage();
	private:
		VideoCapture camera;
		Mat image;
};

#endif
