from config.env import BASE_DIR, env
import stripe  # type: ignore

STRIPE_PUBLISHABLE_KEY = env('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY')
STRIPE_ENDPOINT_SECRET = env('STRIPE_ENDPOINT_SECRET')

stripe.STRIPE_SECRET_KEY = STRIPE_SECRET_KEY
#stripe.WebhookEndpoint = STRIPE_ENDPOINT_SECRET