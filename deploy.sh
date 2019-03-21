#!/bin/bash
aws s3 sync . s3://vue-study --delete
aws cloudfront create-invalidation --distribution-id "E22WVRBHL2XUIP" --paths "/*"

