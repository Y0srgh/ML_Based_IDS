# Given values from the confusion matrix
TP = 576107
TN = 422623
FP = 4
FN = 84

# Accuracy
accuracy = (TP + TN) / (TP + TN + FP + FN)

# Precision
precision = TP / (TP + FP)

# Recall
recall = TP / (TP + FN)

# F1 score
f1_score = 2 * (precision * recall) / (precision + recall)

print("Accuracy",accuracy, "F1_score",f1_score)
