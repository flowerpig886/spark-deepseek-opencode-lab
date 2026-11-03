ARG BASE_IMAGE=tensorfold-dsv41:cb4ceaff2b8c
FROM ${BASE_IMAGE}
COPY engine.py /opt/tensorfold/src/tensorfold/families/deepseek_v41/cuda/engine.py
ENV TF_DS_SINGLE_LANE_CACHE=1
