import * as $protobuf from "protobufjs";

/** Namespace AiTankArenaServer. */
export namespace AiTankArenaServer {

    /** OperationType enum. */
    enum OperationType {
        GET_STATUS = 0,
        JOIN = 1,
        AI_ACTION = 2,
        FRANCE = 3,
        HALT = 4,
        INIT = 5,
        REJOIN = 6,
        SERVER_INFO = 7
    }

    /** Properties of an Operation. */
    interface IOperation {

        /** Operation type */
        type?: (AiTankArenaServer.OperationType | null);

        /** Operation message */
        message?: (string | null);
    }

    /** Represents an Operation. */
    class Operation implements IOperation {

        /** Operation type. */
        public type: AiTankArenaServer.OperationType;
        /** Operation message. */
        public message: string;

        /**
         * Constructs a new Operation.
         * @param [properties] Properties to set
         */
        constructor(properties?: AiTankArenaServer.IOperation);

        /**
         * Creates a new Operation instance using the specified properties.
         * @param [properties] Properties to set
         * @returns Operation instance
         */
        public static create(properties?: AiTankArenaServer.IOperation): AiTankArenaServer.Operation;

        /**
         * Encodes the specified Operation message. Does not implicitly {@link AiTankArenaServer.Operation.verify|verify} messages.
         * @param message Operation message or plain object to encode
         * @param [writer] Writer to encode to
         * @returns Writer
         */
        public static encode(message: AiTankArenaServer.IOperation, writer?: $protobuf.Writer): $protobuf.Writer;

        /**
         * Encodes the specified Operation message, length delimited. Does not implicitly {@link AiTankArenaServer.Operation.verify|verify} messages.
         * @param message Operation message or plain object to encode
         * @param [writer] Writer to encode to
         * @returns Writer
         */
        public static encodeDelimited(message: AiTankArenaServer.IOperation, writer?: $protobuf.Writer): $protobuf.Writer;

        /**
         * Decodes an Operation message from the specified reader or buffer.
         * @param reader Reader or buffer to decode from
         * @param [length] Message length if known beforehand
         * @returns Operation
         * @throws {Error} If the payload is not a reader or valid buffer
         * @throws {$protobuf.util.ProtocolError} If required fields are missing
         */
        public static decode(reader: ($protobuf.Reader | Uint8Array), length?: number): AiTankArenaServer.Operation;

        /**
         * Decodes an Operation message from the specified reader or buffer, length delimited.
         * @param reader Reader or buffer to decode from
         * @returns Operation
         * @throws {Error} If the payload is not a reader or valid buffer
         * @throws {$protobuf.util.ProtocolError} If required fields are missing
         */
        public static decodeDelimited(reader: ($protobuf.Reader | Uint8Array)): AiTankArenaServer.Operation;

        /**
         * Verifies an Operation message.
         * @param message Plain object to verify
         * @returns `null` if valid, otherwise the reason why it is not
         */
        public static verify(message: { [k: string]: any }): (string | null);

        /**
         * Creates an Operation message from a plain object. Also converts values to their respective internal types.
         * @param object Plain object
         * @returns Operation
         */
        public static fromObject(object: { [k: string]: any }): AiTankArenaServer.Operation;

        /**
         * Creates a plain object from an Operation message. Also converts values to other types if specified.
         * @param message Operation
         * @param [options] Conversion options
         * @returns Plain object
         */
        public static toObject(message: AiTankArenaServer.Operation, options?: $protobuf.IConversionOptions): { [k: string]: any };

        /**
         * Converts this Operation to JSON.
         * @returns JSON object
         */
        public toJSON(): { [k: string]: any };
    }
}
