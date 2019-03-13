# Background-Substraction
Used background subtraction and morphological transforms method for detecting the vehicles.
As I was not having a Video Data s I first tried my code on a coin moving, but as the video fps was not upto mark resluts cannot br judged.


After few days I got the video and I have also provided it in the Repo.

I have used Frame Differencing here because it gives much better accuracy than Background Subtraction. Both the methods relay on same base i.e. subtraction of pixels followed by thresholding.

After the moving Vehicles have been segmented, its time to apply some smoothing techniques, which I have used here are Dilation & Erosion. By altering there paramenters you need to find the optimum values for the parameters which will varry from video to video.

Shadows create the worst problem here in this approach. You can also use "cv2.CreateBackgroundSubtractorMOG" as it removes shadows too in the foreground mask. Cool!

After you have the perfectly eroded frames, you can now proceed to draw contours to get location of moving objects.

Then after drawing a rectangle around the moving objects will finaly complete the work for DETECTION!
