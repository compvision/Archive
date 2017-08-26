/* This class should create a GUI if called for in Main. The GUI will be the video capture screen */

#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

class GUIManager
{
    public:
	GUIManager();
	showGUI();
    private:
	Mat frame;
	double distance;
}
