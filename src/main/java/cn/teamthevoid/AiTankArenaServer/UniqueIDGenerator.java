package cn.teamthevoid.AiTankArenaServer;

import java.util.concurrent.atomic.AtomicInteger;

public class UniqueIDGenerator {
    public static AtomicInteger counter = new AtomicInteger(0);

    public static int getNextUniqueID() {
        return counter.getAndIncrement();
    }
}
