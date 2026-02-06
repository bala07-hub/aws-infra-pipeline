from aws_cdk import (
    Stack,
    RemovalPolicy,
    Duration,                # Added for timing
    aws_s3 as s3,
)
from constructs import Construct

class CdkS3BucketStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "demo-cdk-code-catalyst-bala",  
            bucket_name="testing-test-doc-bukall", 
            versioned=True,
            encryption=s3.BucketEncryption.S3_MANAGED,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            enforce_ssl=True,                          # Security Best Practice
            removal_policy=RemovalPolicy.DESTROY,
            
            # --- ADD THIS: Lifecycle Rule ---
            lifecycle_rules=[
                s3.LifecycleRule(
                    enabled=True,
                    expiration=Duration.days(30),      # Auto-delete after 30 days
                    transitions=[
                        s3.Transition(
                            storage_class=s3.StorageClass.INFREQUENT_ACCESS,
                            transition_after=Duration.days(10) # Move to cheaper tier after 10 days
                            # This is a rebase test.
                            "# # final logic"
                        )
                    ]
                )
            ]
        )