#!/bin/bash
echo 'Test 1'
curl --request POST --header 'content-type: application/json' --data @test_1.json --url localhost:5000/predict
echo
echo 'Test 2'
curl --request POST --header 'content-type: application/json' --data @test_2.json --url localhost:5000/predict
