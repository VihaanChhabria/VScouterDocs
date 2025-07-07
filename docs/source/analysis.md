### Analysis

**Use this video for a visual overview on how to import data into analysis and use it:**

[![_](https://img.youtube.com/vi/rIjKhfx3dfQ/0.jpg)](https://www.youtube.com/watch?v=rIjKhfx3dfQ)

Analysis is done through Power BI. You can download it for free [here](https://www.microsoft.com/en-us/power-platform/products/power-bi/downloads).

1. To analyze the CSV data you downloaded at [Parsing Data](#parsing-data) you must download the [Power BI file in this repository](/analysis/VScouter2025Analysis.pbix). Once downloaded, put the `pbix` file into an **empty folder**.
2. Next put you CSV file into the same folder as the `pbix` file. Rename it to `VScouterData.csv`
3. Open the `pbix` file with Power BI. To use this new data click `Transform Data` and then `dataFolderPath`. On this page change the directory to where the `pbix` file and CSV file are located (ex. `C:\Users\username\Documents\Analysis`). **There should not be a `\` at the end.**
4. Click `Close & Apply`.
   ![PowerBIFolderSelection](../readmeimages/PowerBIFolderSelection.gif)

#### Analysis Pages

- **Home Page:** This is the home page where you can go to the other analysis pages easily. **To click on the buttons, you press `ctrl+click`.**

![PowerBIHomePage](../readmeimages/PowerBIHomePage.png)

- **Game Dashboard:** On this page you can look the max, min, and medians of each team in total points, auto points, teleop points, coral points, and algae points. The top 5 are shown on this page. Clicking the arrow next to each graph will bring you to a specific page to it so you can see all of the teams. **During alliance selection, if a team is picked and you do not want to see their statistics, you can click the `Filter` panel to open it and filter the team out of the `selectTeam` filter in the `Filters on all pages` section.**

![PowerBIGameDashboard](../readmeimages/PowerBIGameDashboard.png)

- **Team Abilities:** Here you can see a teams overall data. To change the team selected, you can use the list selection.

![PowerBITeamAbilities](../readmeimages/PowerBITeamAbilities.png)

- **Team Performance Over Time:** On this page you can see a teams performance over their matches played. This is scene in 5 graphs: total points, auto points, teleop points, algae points, and coral points. To change the team selected, you can use the list selection.

![PowerBIAutoNotesOverview](../readmeimages/PowerBITeamPerformanceOverTime.png)

- **Scouter Match Numbers:** On this page you can see how many matches a scouter has scouted. This is shown by a graph of each scouter initial and how many matches they have scouted.

![PowerBIScouterMatchNumbers](../readmeimages/PowerBIScouterMatchNumbers.png)
