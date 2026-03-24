import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from issues.models import Reporter, Issue, CriticalIssue, LowPriorityIssue


@csrf_exempt
def reporters(request):

    if request.method == "POST":
        
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON body"}, status=400)

        required = ["id", "name", "email", "team"]
        missing  = [f for f in required if f not in data]
        if missing:
            return JsonResponse(
                {"error": f"Missing required fields: {', '.join(missing)}"}, status=400
            )
        
        reporter = Reporter(data["id"], data["name"], data["email"], data["team"])

        try:
            reporter.validate()
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

        # save to file
        f = open("reporters.json", "r")
        reporters_list = json.load(f)
        f.close()

        reporters_list.append(reporter.to_dict())

        f = open("reporters.json", "w")
        json.dump(reporters_list, f)
        f.close()

        return JsonResponse(reporter.to_dict(), status=201)

    elif request.method == "GET":
        f = open("reporters.json", "r")
        reporters_list = json.load(f)
        f.close()

        reporter_id = request.GET.get("id")

        if reporter_id:
            for reporter in reporters_list:
                if reporter["id"] == int(reporter_id):
                    return JsonResponse(reporter, status=200)
            return JsonResponse({"error": "Reporter not found"}, status=404)

        return JsonResponse(reporters_list, safe=False, status=200)


@csrf_exempt
def issues(request):

    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON body"}, status=400)

        required = ["id", "title", "description", "status", "priority", "reporter_id"]
        missing  = [f for f in required if f not in data]
        if missing:
            return JsonResponse(
                {"error": f"Missing required fields: {', '.join(missing)}"}, status=400
            )

        # pick the right class based on priority
        if data["priority"] == "critical":
            issue = CriticalIssue(data["id"], data["title"], data["description"], data["status"], data["priority"], data["reporter_id"])
        elif data["priority"] == "low":
            issue = LowPriorityIssue(data["id"], data["title"], data["description"], data["status"], data["priority"], data["reporter_id"])
        else:
            issue = Issue(data["id"], data["title"], data["description"], data["status"], data["priority"], data["reporter_id"])

        try:
            issue.validate()
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

        # save to file
        f = open("issues.json", "r")
        issues_list = json.load(f)
        f.close()

        issues_list.append(issue.to_dict())

        f = open("issues.json", "w")
        json.dump(issues_list, f)
        f.close()

        response_data = issue.to_dict()
        response_data["message"] = issue.describe()
        return JsonResponse(response_data, status=201)

    elif request.method == "GET":
        f = open("issues.json", "r")
        issues_list = json.load(f)
        f.close()

        issue_id = request.GET.get("id")
        if issue_id:
            for issue in issues_list:
                if issue["id"] == int(issue_id):
                    return JsonResponse(issue, status=200)
            return JsonResponse({"error": "Issue not found"}, status=404)

        status = request.GET.get("status")
        if status:
            filtered = []
            for issue in issues_list:
                if issue["status"] == status:
                    filtered.append(issue)
            return JsonResponse(filtered, safe=False, status=200)

        return JsonResponse(issues_list, safe=False, status=200)
