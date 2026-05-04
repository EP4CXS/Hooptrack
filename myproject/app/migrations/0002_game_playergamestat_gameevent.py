from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Game",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("team1_name", models.CharField(max_length=100)),
                ("team2_name", models.CharField(max_length=100)),
                ("score1", models.IntegerField(default=0)),
                ("score2", models.IntegerField(default=0)),
                ("quarter", models.IntegerField(default=1)),
                ("clock", models.CharField(default="12:00", max_length=16)),
                ("status", models.CharField(choices=[("in-progress", "In Progress"), ("completed", "Completed")], default="in-progress", max_length=20)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("bracket", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="app.bracket")),
                ("matchup", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="app.matchup")),
            ],
            options={"ordering": ["-updated_at"]},
        ),
        migrations.CreateModel(
            name="PlayerGameStat",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("team_name", models.CharField(max_length=100)),
                ("fgm2", models.IntegerField(default=0)),
                ("fga2", models.IntegerField(default=0)),
                ("fgm3", models.IntegerField(default=0)),
                ("fga3", models.IntegerField(default=0)),
                ("ftm", models.IntegerField(default=0)),
                ("fta", models.IntegerField(default=0)),
                ("oreb", models.IntegerField(default=0)),
                ("dreb", models.IntegerField(default=0)),
                ("assists", models.IntegerField(default=0)),
                ("steals", models.IntegerField(default=0)),
                ("blocks", models.IntegerField(default=0)),
                ("fouls", models.IntegerField(default=0)),
                ("turnovers", models.IntegerField(default=0)),
                ("points", models.IntegerField(default=0)),
                ("game", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="player_stats", to="app.game")),
                ("player", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="app.player")),
            ],
            options={"ordering": ["team_name", "player__name"], "unique_together": {("game", "player")}},
        ),
        migrations.CreateModel(
            name="GameEvent",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("team_name", models.CharField(max_length=100)),
                ("event_type", models.CharField(choices=[("made2", "Made 2"), ("missed2", "Missed 2"), ("made3", "Made 3"), ("missed3", "Missed 3"), ("madeFT", "Made FT"), ("missedFT", "Missed FT"), ("oreb", "Offensive Rebound"), ("dreb", "Defensive Rebound"), ("assist", "Assist"), ("steal", "Steal"), ("block", "Block"), ("foul", "Foul"), ("turnover", "Turnover")], max_length=20)),
                ("quarter", models.IntegerField(default=1)),
                ("game_time", models.CharField(default="12:00", max_length=16)),
                ("description", models.TextField(blank=True, default="")),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("game", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="events", to="app.game")),
                ("player", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="app.player")),
            ],
            options={"ordering": ["created_at"]},
        ),
    ]
