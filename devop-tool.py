import subprocess
import sys


def run(cmd):
    """Run shell command safely"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip()


def print_section(title):
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)


def check_pods():
    out, err = run("kubectl get pods")
    print(out)


def check_services():
    out, err = run("kubectl get svc")
    print(out)


def check_helm():
    out, err = run("helm list")
    print(out)


def cluster_info():
    out, err = run("kubectl cluster-info")
    print(out)


def restart_frontend():
    print("Restarting frontend deployment...")
    out, err = run("kubectl rollout restart deployment frontend")
    print(out or err)


def helm_upgrade():
    print("Running Helm upgrade...")
    out, err = run("helm upgrade blood-app ./Helm")
    print(out or err)


def main():
    print_section("KUBERNETES CLUSTER HEALTH CHECK")

    print("\n📦 Cluster Info:")
    cluster_info()

    print_section("PODS STATUS")
    check_pods()

    print_section("SERVICES STATUS")
    check_services()

    print_section("HELM RELEASE STATUS")
    check_helm()

    if "--restart-frontend" in sys.argv:
        print_section("RESTARTING FRONTEND")
        restart_frontend()

    if "--deploy" in sys.argv:
        print_section("HELM DEPLOYMENT TRIGGERED")
        helm_upgrade()

    print("\n✅ DONE")


if __name__ == "__main__":
    main()