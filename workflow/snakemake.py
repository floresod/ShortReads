import glob

SAMPLE,RF=glob_wildcards("../resources/Data/{sample}_{rf}.fastq")

rule all:
    input: 
        expand("../resources/Outputs/fastqc_rr/{sample}_{rf}.html", sample=SAMPLE, rf=RF), 
        expand("../resources/Outputs/fastqc_rr/{sample}_{rf}_fastqc.zip", sample=SAMPLE, rf=RF)

rule fastqc_rr:
    input: 
        reads="../resources/Data/{sample}_{rf}.fastq"
    output: 
        html="../resources/Outputs/fastqc_rr/{sample}_{rf}.html",
        zip="../resources/Outputs/fastqc_rr/{sample}_{rf}_fastqc.zip"
    params:
        extra="--quiet"
    threads:
        4
    resources:
        mem_mb=4000
    log:
        "../resources/Logs/fastqc_rr/{sample}_{rf}.log"
    conda:
        "../envs/fastqc_env.yaml"
    wrapper:
        "v4.5.0/bio/fastqc"


