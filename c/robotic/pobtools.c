#include <pobRoboticSuite.h>


#define DISTANCE        150
#define SPEED           100
#define RADIUS          95
#define BLACK           100
#define NUM_MAX_LOOPS   30
#define INTERVAL        100

int main(void) {
    Status status;
    LineSensor result;

    const int kp = 2, ki = 0, kd = 0;
    int error, last_error = 0, integral = 0, deriv;
    int corr;
    int num_loops = 0;

    // Robot initialisation.
    InitCpu();
    InitRobot();
    InitUART0(115200);

    // Turn right the distance sensor.
    SetServo(1, 0, 31);
    WaitMs(500);

    // Wall tracking.
    do {
        error = DISTANCE - GetDistanceSensor(1);
        integral += error;
        deriv = error - last_error;

        corr = (kp * error + ki * integral + kd * deriv) / 10;
        SetMotor(SPEED - corr, SPEED + corr);

        last_error = error;

        // Rotation near a wall in front of the robot.
        if (GetDistanceSensor(2) < DISTANCE) {
            DoRotation(RADIUS, SPEED);

            do {
                GetStatus(&status);
            } while (status.eventDoRotation != 0);
        }

        GetValuesFromLineSensor(2, &result);
        WaitMs(INTERVAL);

        // Stop tracking the wall, when a black line was found.
    } while (result.left >= BLACK && result.right >= BLACK);


    // The robot advances a little before turning around to find the black line.
    SetMotor(SPEED, SPEED);
    WaitMs(500);
    DoRotation(180, 50);

    do {
        GetValuesFromLineSensor(2, &result);
        GetStatus(&status);
    } while (status.eventDoRotation != 0 && (result.left >= BLACK && result.right >= BLACK));


    // Line tracking.
    // The robot turns right or left according the sensor that finds the line.
    do {
        // Check if the line is not just below the robot, before stopping tracking.
        if (num_loops == NUM_MAX_LOOPS - 1) {
            DoRotation(10, SPEED);

            do {
                GetValuesFromLineSensor(2, &result);
                GetStatus(&status);
            } while (status.eventDoRotation != 0
                     && (result.left >= BLACK && result.right >= BLACK));
        }

        SetMotor(SPEED - 30, SPEED - 30);
        GetValuesFromLineSensor(2, &result);

        if (result.left < BLACK) {
            num_loops = 0;
            DoRotation(5, 31);

            do {
                GetStatus(&status);
            } while (status.eventDoRotation != 0);
        }

        if (result.right < BLACK) {
            num_loops = 0;
            DoRotation(-5, 31);

            do {
                GetStatus(&status);
            } while (status.eventDoRotation != 0);
        }

        num_loops++;
        WaitMs(INTERVAL);

        // Stop the tracking when the line was not found during NUM_MAX_LOOPS turns.
    } while (num_loops < NUM_MAX_LOOPS);


    // Stop the robot, it's the end.
    SetMotor(0, 0);

    return 0;
}
