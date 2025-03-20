# MCnet/MCviz Task 2

## Instructions to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/Yash-g2310/Mcnet_MCviz_task.git
cd Mcnet_MCviz_task
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Run the Code
- **Task 2a and 2b**: The code is in `task2.ipynb`. Open and run each cell to execute the code.
  - `basic_event_info.txt` is the output file for task 2a, containing generic information for each event.
  - `particle_interaction_networkx.html` is the output file for task 2b, produced by Plotly to visualize the Feynman diagram interactively.
- **Task 2c**: The main code is in `app.py`. Run the following command:
    ```bash
    flask --app app run
    ```
  - Navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) for further information.
  - `event_info_json.json` is the file from which each endpoint is served.

## Project Structure

```
MCnet_MCviz_task/
├── output/
│   ├── basic_event_info.txt
│   ├── event_info_json.json
│   └── particle_interaction_networkx.html
├── app.py
├── README.md
├── requirements.txt
├── task2.ipynb
└── top.lhe
```
