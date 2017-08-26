/* This class contains the basic framework for targeting
 * the text books. The program will take an image, threshold it,
 * run Canny edge detector and send it off to TargetDetector.
 * Author: Ethan Yao
 */
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;


class Target
{
    private:
	Mat img;
	Mat img_hsv;
    public:
	Mat threshold(Mat img, low, high);
	Mat Canny(Mat img);
}


