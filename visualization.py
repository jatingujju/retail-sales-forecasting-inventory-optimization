import matplotlib.pyplot as plt
import pandas as pd


def plot_sales_trend(df):
    """
    Plot overall sales trend
    """
    df_grouped = df.groupby("date")["qty_sold"].sum()

    plt.figure()
    plt.plot(df_grouped.index, df_grouped.values)
    plt.title("📈 Total Sales Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("sales_trend.png")
    plt.show()


def plot_actual_vs_predicted(y_true, y_pred):
    """
    Plot actual vs predicted values
    """
    plt.figure()
    plt.plot(y_true[:100].values, label="Actual")
    plt.plot(y_pred[:100], label="Predicted")
    plt.title("📊 Actual vs Predicted Sales")
    plt.legend()

    plt.savefig("actual_vs_predicted.png")
    plt.show()


def plot_feature_importance(model, feature_names):
    """
    Plot feature importance
    """
    importance = model.feature_importances_

    plt.figure()
    plt.barh(feature_names, importance)
    plt.title("📌 Feature Importance")
    plt.tight_layout()

    plt.savefig("feature_importance.png")
    plt.show()