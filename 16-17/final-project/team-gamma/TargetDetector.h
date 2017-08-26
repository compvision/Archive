/* This class receives input from Target which should be in the format
 * of a Cannied image. It will attempt to find any rectangles in the 
 * image and send this (these) contours to TargetProcessor for further
 * processing. Should probably be static
 * Author: Ethan Yao
 */
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

class TargetDetector
{
    private:
	Mat frame;
    public:
	Mat findRectangles(Mat img);
}
