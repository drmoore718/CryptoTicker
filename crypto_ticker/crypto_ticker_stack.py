import aws_cdk.core as cdk
import aws_cdk.aws_apigateway as agw

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class CryptoTickerStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        api = agw.RestApi(self, 'cryptoTicker',
            endpoint_types=[agw.EndpointType.REGIONAL],
            deploy_options=agw.StageOptions(
                metrics_enabled=True
            )
        )

        with open('crypto_ticker/ticker.html','r') as f:
            ticker = f.read()

        api.root.add_resource('ticker', default_integration=agw.MockIntegration(
            integration_responses=[
                agw.IntegrationResponse(
                    status_code='200',
                    response_parameters={
                        'method.response.header.Content-Type': '\'text/html\'',
                        'method.response.header.Cache-Control': '\'max-age=300\''
                    },
                    response_templates={
                        'text/html': ticker
                    }
                )
            ],
            passthrough_behavior=agw.PassthroughBehavior.NEVER,
            request_templates={
                'application/json': '{"statusCode": 200}'
            }
        )).add_method('GET',
            method_responses=[{
                'statusCode': '200',
                'responseParameters': {
                    'method.response.header.Content-Type': True,
                    'method.response.header.Cache-Control': True
                },
                'responseModels': {
                    'text/html': api.add_model('ResponseModel',
                        content_type='text/html',
                        model_name='ResponseModel',
                        schema=agw.JsonSchema()
                    )
                }
            }],
        )
