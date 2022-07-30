{
    "Comment": "Workflow execute when new roofer created",
    "StartAt": "CreateRoofingContractor",
    "States": {
        "CreateRoofingContractor": {
            "Type": "Task",
            "Resource": "arn:aws:lambda:us-east-1:906360379090:function:new-roofing-contractor-workflow-dev-create_business",
            "Retry": [
                {
                    "ErrorEquals": ["CustomError"],
                    "IntervalSeconds": 1,
                    "MaxAttempts": 2,
                    "BackoffRate": 2.0
                },
                {
                    "ErrorEquals": ["States.TaskFailed"],
                    "IntervalSeconds": 30,
                    "MaxAttempts": 2,
                    "BackoffRate": 2.0
                },
                {
                    "ErrorEquals": ["States.ALL"],
                    "IntervalSeconds": 5,
                    "MaxAttempts": 5,
                    "BackoffRate": 2.0
                }
            ],
            "Next": "Echo"
        },
        "Echo": {
            "Type": "Task",
            "Resource": "arn:aws:lambda:us-east-1:906360379090:function:new-roofing-contractor-workflow-dev-echo",
            "Retry": [
                {
                    "ErrorEquals": ["CustomError"],
                    "IntervalSeconds": 1,
                    "MaxAttempts": 2,
                    "BackoffRate": 2.0
                },
                {
                    "ErrorEquals": ["States.TaskFailed"],
                    "IntervalSeconds": 30,
                    "MaxAttempts": 2,
                    "BackoffRate": 2.0
                },
                {
                    "ErrorEquals": ["States.ALL"],
                    "IntervalSeconds": 5,
                    "MaxAttempts": 5,
                    "BackoffRate": 2.0
                }
            ],
            "End": true
        }
    }
}
