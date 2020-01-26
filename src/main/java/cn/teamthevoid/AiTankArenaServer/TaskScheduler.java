package cn.teamthevoid.AiTankArenaServer;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class TaskScheduler {
    List<Task> uncompletedTasks = new ArrayList<>();

    public synchronized TaskScheduler addTask(Task task) {
        uncompletedTasks.add(task);
        return this;
    }

    public synchronized TaskScheduler perform() {
        uncompletedTasks.forEach(Task::run);
        return this;
    }

    public synchronized TaskScheduler randomPerform() {
        Collections.shuffle(uncompletedTasks);
        perform();
        return this;
    }


}
