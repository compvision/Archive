#include <opencv2/opencv.hpp>
#include "Target.hpp"
using namespace cv;

class targetProcessing
{
    public:

        targetProcessing();
        void loadTarget(Target* target);
        double Distance();
        double Azimuth();
        double Altitude();

    private:

        double targetWidth;
        double objectWidth;
        Point targetCenter;
        double focalLength;
        double horizCenter;
        double vertCenter;

};
