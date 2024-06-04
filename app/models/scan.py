class User:
    def __init__(self, id, requested_by, started_at, finished_at, name, status, scanners, severity_counts, assets_scanned):
        self.id = id
        self.requested_by = requested_by
        self.started_at = started_at
        self.finished_at = finished_at
        self.name = name
        self.status = status
        self.scanners = scanners
        self.severity_counts = severity_counts
        self.assets_scanned = assets_scanned


    def to_dict(self):
        return {
            "id": self.id,
            "requested_by": self.requested_by,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "name": self.name,
            "status": self.status,
            "scanners": self.scanners,
            "severity_counts": self.severity_counts,
            "assets_scanned": self.assets_scanned
        }