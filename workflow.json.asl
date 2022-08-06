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
            "Next": "RooferExistsChoice"
        },
        "RooferExistsChoice": {
            "Type": "Choice",
            "Choices": [
                {
                    "Variable": "$.roofer_exists",
                    "BooleanEquals": true,
                    "Next": "SendMessagePublicChannel" 
                },
                {
                    "Variable":"$.roofer_exists",
                    "BooleanEquals": false,
                    "Next": "CheckStripeCustomerExists"
                }
            ]
        },
        "CheckStripeCustomerExists": {
            "Type": "Task",
            "Resource": "arn:aws:lambda:us-east-1:906360379090:function:new-roofing-contractor-workflow-dev-has_stripe_customer",
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
            "Next": "ifCustomerExists"
        },
        "ifCustomerExists": {
            "Type": "Choice",
            "Choices": [
                {
                    "Variable": "$.stripeCustomerExists",
                    "BooleanEquals": false,
                    "Next": "CreateStripeCustomer"
                },
                {
                    "Variable": "$.stripeCustomerExists",
                    "BooleanEquals": true,
                    "Next": "AddStripeIdToRooferRecord"
                }
            ]
        },
        "CreateStripeCustomer": {
            "Type": "Task",
            "Resource": "arn:aws:lambda:us-east-1:906360379090:function:new-roofing-contractor-workflow-dev-create_stripe_customer",
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
            "Next": "AddStripeIdToRooferRecord" 
        },
        "AddStripeIdToRooferRecord": {
            "Type": "Task",
            "Resource": "arn:aws:lambda:us-east-1:906360379090:function:new-roofing-contractor-workflow-dev-add_stripe_customer_dynamo",
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
            "Next": "SendMessagePublicChannel"
        },
        "SendMessagePublicChannel": {
            "Type": "Task",
            "Resource": "arn:aws:lambda:us-east-1:906360379090:function:new-roofing-contractor-workflow-dev-send_slack_message",
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
