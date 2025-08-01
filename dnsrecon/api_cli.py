#!/usr/bin/env python3
import argparse
import os

import uvicorn


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-H',
        '--host',
        default='127.0.0.1',
        help='IP address to listen on default is 127.0.0.1',
    )
    parser.add_argument(
        '-p',
        '--port',
        default=5000,
        help='Port to bind the web server to, default is 5000',
        type=int,
    )
    parser.add_argument(
        '-l',
        '--log-level',
        default='info',
        help='Set logging level, default is info but [critical|error|warning|info|debug|trace] can be set',
    )
    parser.add_argument(
        '-r',
        '--reload',
        default=False,
        help='Enable automatic reload used during development of the api',
        action='store_true',
    )
    parser.add_argument(
        '--rate-limit',
        default='5/minute',
        help='Set API rate limit (e.g., "10/minute", "100/hour"), default is 5/minute',
    )

    args: argparse.Namespace = parser.parse_args()

    # Set environment variable for API rate limit
    os.environ['API_RATE_LIMIT'] = args.rate_limit

    uvicorn.run(
        'dnsrecon.api:app',
        host=args.host,
        port=args.port,
        log_level=args.log_level,
        reload=args.reload,
    )


if __name__ == '__main__':
    main()
