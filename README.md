# EuRoC 23 Team Data
This repository includes all data collected by CATS during EuRoC 2023.

## Structure

For each team, the data collected by telemetry is presented. If the rocket was recovered with a functioning CATS Vega, the flight log is also added to the repository.
Some flight computers were tracked with two ground stations. In this case, they have the same name, but one of the two logs has an added `_1`.

 ## Plotting of Ground Station Data

 For plotting, we provide a very quickly hacked up jupyter notebook for the ground station data. Use at your own risk.

 ## Plotting of CATS Flight Log (.cfl)

 For plotting the .cfl file, please download the [CATS Configurator](https://github.com/catsystems/cats-configurator/releases) and drag and drop the file. You can then export the data to .csv for further processing. Make sure to update the configurator to 0.3.4, as on 0.3.3 the configurator fails if no GNSS data is recorded. Also, the .csv file is saved in the installation folder. This will be fixed in an upcoming release.

 ## Adding your SRAD Data

 If you want to add the data which you collected during your flight or want to add a README in your team's folder to discuss some things, feel free to do so! We will merge all pull requests adding data!
