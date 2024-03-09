import pandas as pd;
from sklearn.ensemble import RandomForestClassifier;
import joblib;  # Hoặc sử dụng thư viện pickle

# B1 Đọc dữ liệu và hiểu dữ liệu
df = pd.read_csv('../static/clean_dataset.csv', delimiter=',');


X = df.drop(['class'], axis=1);          
y = df['class'];                              # cột nhãn

# ---------------------------------------------------------------------------------------------
# Huấn luyện mô hình Random Forest
rf_model = RandomForestClassifier(n_estimators=50, criterion='entropy', random_state=42);
rf_model.fit(X, y);

# Lưu mô hình vào một tệp
joblib.dump(rf_model, 'rf_model.pkl');


#  # Huấn luyện mô hình trên tập dữ liệu huấn luyện
# rf_model.fit(X, y);

# # Dự đoán trên tập kiểm tra
# new_data = pd.DataFrame([[2, 3, 0, 1, 0, 0, 0, 2]], columns=X.columns)
# y_pred = rf_model.predict(new_data);

# print("KET QUA: ", y_pred);

