# Loan Approval Model Flow

```mermaid
flowchart LR
    A[loans.csv] --> B[Select features]
    B --> C[income\ncredit_score\nloan_amount\nemployment_years]
    A --> D[Select target]
    D --> E[loan_status\n0 = rejected\n1 = approved]
    C --> F[80% training data]
    C --> G[20% test data]
    E --> F
    E --> G
    F --> H[Logistic Regression\nscaled numeric features]
    F --> I[Random Forest\nmultiple decision trees]
    H --> J[Soft voting ensemble]
    I --> J
    J --> K[Approval prediction]
    G --> L[Evaluate accuracy\nprecision, recall, F1]
```

The two models learn from the same applicant features. Logistic Regression captures a simpler linear relationship, while Random Forest can capture more complex feature interactions. A soft-voting ensemble combines their predicted probabilities before choosing the final class.
