import sys
import statsapi
import datetime
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox
from PyQt6.QtCore import QTimer, Qt, QThread, pyqtSignal

class ScoreFetcher(QThread):
    score_fetched = pyqtSignal(str)

    def __init__(self, gamepk):
        QThread.__init__(self)
        self.gamepk = gamepk
        self.running = True

    def run(self):
        if self.gamepk != None:
            try:
                score_info = statsapi.linescore(gamePk=self.gamepk)
                self.score_fetched.emit(score_info)
            except:
                self.score_fetched.emit("Error fetching score")

class MLBScoreTracker(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("MLB Live Score Tracker")
        self.setGeometry(100, 100, 400, 200)
        self.layout = QVBoxLayout()
        
        self.team_selector = QComboBox(self)
        self.teams = statsapi.lookup_team('')
        self.team_map = {}
        for team in self.teams:
            self.team_map[team['name']] = team['id']
            self.team_selector.addItem(team['name'])
        self.team_selector.currentTextChanged.connect(self.update_game_id)
        self.layout.addWidget(self.team_selector)
        
        self.label = QLabel("Select a team to get live scores", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.label)
        
        self.stop_button = QPushButton("Stop", self)
        self.stop_button.clicked.connect(self.close)
        self.layout.addWidget(self.stop_button)
        
        self.setLayout(self.layout)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.fetch_score)
        self.timer.start(10000)
        
        self.gamepk = None
        self.update_game_id()

    def resizeEvent(self, event):
        parent_width = self.width()
        parent_height = self.height()

        width_factor = 0.9
        height_factor = 0.2

        new_width = int(parent_width * width_factor)
        new_height = int(parent_height * height_factor)

        self.label.setFixedSize(new_width, new_height)
        self.label.setStyleSheet(f"font-size: {max(10, new_height // 4)}px;")

        super().resizeEvent(event)

    def update_game_id(self):
        team_name = self.team_selector.currentText()
        if team_name in self.team_map:
            team_id = self.team_map[team_name]
            date = datetime.datetime.today().strftime("%m/%d/%Y")
            schedule = statsapi.schedule(team=team_id, start_date=date, end_date=date)
            if len(schedule) > 0:
                self.gamepk = schedule[0]['game_id']
                self.fetch_score()
            else:
                self.gamepk = None
                self.label.setText("No active game found for today.")
        else:
            self.label.setText("Invalid team selection.")

    def fetch_score(self):
        if self.gamepk != None:
            self.thread = ScoreFetcher(self.gamepk)
            self.thread.score_fetched.connect(self.display_score)
            self.thread.start()
        else:
            self.label.setText("No active game found for today.")

    def display_score(self, score):
        self.label.setText(score)

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("Astroslogo.ico"))
window = MLBScoreTracker()
window.show()
sys.exit(app.exec())