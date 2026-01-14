from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Database: {MAC_ADDR_SIGNAL_STRENGTHS: ROOM_ID}
# Training Data: [[Router1_RSSI, Router2_RSSI, Router3_RSSI]]
X_train = np.array([
    [-50, -70, -80], # Room 101
    [-80, -40, -90], # Room 102
    [-60, -60, -40]  # Lab 1
])
y_train = ['Room 101', 'Room 102', 'Lab 1']

def find_me(current_rssi):
    """K-Nearest Neighbors predicts location based on signal strength."""
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(X_train, y_train)
    prediction = model.predict([current_rssi])
    return f"📍 Predicted Location: {prediction[0]}"

# Current environment scan (No GPS needed!)
print(find_me([-52, -68, -78]))