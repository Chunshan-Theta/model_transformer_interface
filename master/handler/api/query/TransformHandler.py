import json

from handler.api.apiHandlerBase import APIHandlerBase
from util.aredis_queue import QueueRequestTask
import asyncio


class TransformMBTI2MyersHandler(APIHandlerBase):

    async def post(self):
        """
        ---
        tags:
        - model
        summary: List posts
        description: List all posts in feed
        produces:
        - application/json
        parameters:
        -   in: body
            name: body
            description: post data
            required: true
            schema:
                type: object
                properties:

                    input_array:
                        type: array
                        items:
                            type: float
                        default: [
                            0.01,
                            0.2,
                            0.86,
                            0.03
                        ]
        responses:
            200:
              description: test
        """
        #EI
        #NS
        #TF
        #JP
        # 「外向（E）」與「內向（I）」
        # 「直覺（N）」與「實感（S）」
        # 「思考（T）」與「情感（F）」
        # 「判斷（J）」與「感知（P）」
        body = json.loads(self.request.body)
        input_array = body.get("input_array", None)
        if len(input_array) != 4:
            return self.write_json({
                "status": "405",
                "data": f"ERROR INPUT: {input_array}"
            })
        transform_array = [
            [0.35,0.1,0.1,0.45], #建議
            [0.15,0.15,0.25,0.45], #分析
            [0.45,0.25,0.15,0.15], #肯定
            [0.25,0.35,0.15,0.15], #安撫
            [0.45,0.20,0.20,0.15], #陪伴
            [0.40,0.30,0.15,0.15], #表達感謝
            [0.15,0.25,0.30,0.30]  #評價
        ]

        result=[]
        for weight_array in transform_array:
            result.append(sum([value*weight for value, weight in zip(input_array,weight_array)]))

        return self.write_json({
            "status": "success",
            "data": result
        })


