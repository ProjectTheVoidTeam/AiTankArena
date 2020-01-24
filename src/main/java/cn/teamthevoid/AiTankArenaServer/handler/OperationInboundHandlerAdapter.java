package cn.teamthevoid.AiTankArenaServer.handler;

import cn.teamthevoid.AiTankArenaServer.message.operation.Operation;
import cn.teamthevoid.AiTankArenaServer.message.operation.OperationType;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;

public abstract class OperationInboundHandlerAdapter extends ChannelInboundHandlerAdapter {

    abstract OperationType getOperationType();

    abstract void channelRead(ChannelHandlerContext ctx, Operation operation);

    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
        Operation operation = (Operation) msg;
        if (operation.getType().equals(getOperationType())) {
            channelRead(ctx, operation);
        } else ctx.fireChannelRead(msg);
    }

    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) { // (4)
        cause.printStackTrace();
        ctx.close();
    }

}
