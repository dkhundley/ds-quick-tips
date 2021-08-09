docker build -t iris-api:dev -f ../Dockerfile
export CONTAINER_ID=$(docker run -d -p 5001:5001 iris-api:dev)
bash run_container_scan.sh
bash run_dependency_scan.sh
bash run_linter.sh
bash run_perf_test.sh
bash run_static_scan.sh
bash run_unit_tests.sh
docker stop $CONTAINER_ID