import pandas as pd
import matplotlib.pyplot as plt
import os

# Base directory
base_dir = './'  # Assuming the script is in the same directory as the folders

# List all directories in the base directory
directories = [dir for dir in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, dir))]

# Iterate over each directory
for dir in directories:
    csv_files = [f for f in os.listdir(os.path.join(base_dir, dir)) if f.endswith('.csv')]
    
    # Filter for files with the word "main" or take any if no match found
    main_files = [f for f in csv_files if 'main' in f]
    if main_files:
        file_to_read = main_files[0]
    else:
        file_to_read = csv_files[0] if csv_files else None

    if file_to_read:
        # Reading data
        file_path = os.path.join(base_dir, dir, file_to_read)
        log = pd.read_csv(file_path)
        # Take logs only from the first link
        log = log[log['link'] == 1].reset_index()
        
        # Create a 'plots' subfolder inside the current directory if it doesn't exist
        plots_folder = os.path.join(base_dir, dir, 'plots')
        os.makedirs(plots_folder, exist_ok=True)

        # Compute adjusted time
        min_time = log["ts[deciseconds]"].min()
        adjusted_time = (log["ts[deciseconds]"] - min_time) / 10

        # Matplotlib plot for Altitude
        plt.figure(figsize=(8, 6), dpi=300)
        plt.plot(adjusted_time, log["altitude[m]"])
        plt.title('Altitude vs Time')
        plt.xlabel('Time [s]')
        plt.ylabel('Altitude [m]')
        plt.grid(True)
        # Add vertical lines based on state change
        for i in range(1, len(log)):
            if log['state'][i] != log['state'][i-1]:
                plt.axvline(x=adjusted_time[i], linewidth=1, linestyle='--', color='red')
        plt.tight_layout()
        plt.savefig(os.path.join(plots_folder, 'altitude.png'), dpi=300)
        plt.close()

        # Matplotlib plot for Velocity
        plt.figure(figsize=(8, 6), dpi=300)
        plt.plot(adjusted_time, log["velocity[m/s]"])
        plt.title('Velocity vs Time')
        plt.xlabel('Time [s]')
        plt.ylabel('Velocity [m/s]')
        plt.grid(True)
        # Add vertical lines based on state change
        for i in range(1, len(log)):
            if log['state'][i] != log['state'][i-1]:
                plt.axvline(x=adjusted_time[i], linewidth=1, linestyle='--', color='red')
        plt.tight_layout()
        plt.savefig(os.path.join(plots_folder, 'velocity.png'), dpi=300)
        plt.close()

        # Formatting team name
        formatted_team_name = ' '.join([word.upper() for word in dir.split('_')])
        
        # Create README
        max_altitude = log["altitude[m]"].max()
        with open(os.path.join(base_dir, dir, 'README.md'), 'w') as readme:
            readme.write(f"# {formatted_team_name}\n")
            readme.write(f"## Flight Statistics\n")
            readme.write(f"Maximum Reached Altitude: {max_altitude} m\n\n")
            readme.write(f"![Altitude Plot](./plots/altitude.png)\n\n")
            readme.write(f"![Velocity Plot](./plots/velocity.png)\n\n")

print("Plots generated!")
