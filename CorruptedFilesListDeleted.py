# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 18:18:40 2024

@author: Anish
"""

import os

# Replace this with the directory path where the files are located
directory_path = r"C:\Users\Anish\OneDrive\Desktop\Project I\train\0"

# List of files to delete
files_to_delete = [
    "F_1574.jpg", "F_2247.jpg", "F_585.jpg", "F_586.jpg", "F_587.jpg", "F_589.jpg", "F_59.jpg", "F_590.jpg",
    "F_591.jpg", "F_592.jpg", "F_593.jpg", "F_595.jpg", "F_596.jpg", "F_597.jpg", "F_598.jpg", "F_599.jpg",
    "F_60.jpg", "F_600.jpg", "F_601.jpg", "F_602.jpg", "F_603.jpg", "F_604.jpg", "F_605.jpg", "F_606.jpg",
    "F_607.jpg", "F_608.jpg", "F_609.jpg", "F_61.jpg", "F_610.jpg", "F_611.jpg", "F_612.jpg", "F_613.jpg",
    "F_614.jpg", "F_615.jpg", "F_616.jpg", "F_617.jpg", "F_618.jpg", "F_619.jpg", "F_62.jpg", "F_620.jpg",
    "F_621.jpg", "F_622.jpg", "F_623.jpg", "F_624.jpg", "F_625.jpg", "F_626.jpg", "F_627.jpg", "F_628.jpg",
    "F_629.jpg", "F_63.jpg", "F_630.jpg", "F_631.jpg", "F_632.jpg", "F_633.jpg", "F_634.jpg", "F_635.jpg",
    "F_636.jpg", "F_637.jpg", "F_638.jpg", "F_639.jpg", "F_64.jpg", "F_640.jpg", "F_641.jpg", "F_642.jpg",
    "F_643.jpg", "F_644.jpg", "F_645.jpg", "F_646.jpg", "F_647.jpg", "F_648.jpg", "F_649.jpg", "F_65.jpg",
    "F_650.jpg", "F_651.jpg", "F_652.jpg", "F_653.jpg", "F_654.jpg", "F_655.jpg", "F_656.jpg", "F_657.jpg",
    "F_658.jpg", "F_659.jpg", "F_66.jpg", "F_660.jpg", "F_661.jpg", "F_662.jpg", "F_663.jpg", "F_664.jpg",
    "F_665.jpg", "F_666.jpg", "F_667.jpg", "F_668.jpg", "F_669.jpg", "F_67.jpg", "F_670.jpg", "F_671.jpg",
    "F_672.jpg", "F_673.jpg", "F_674.jpg", "F_675.jpg", "F_676.jpg", "F_677.jpg", "F_678.jpg", "F_679.jpg",
    "F_68.jpg", "F_680.jpg", "F_681.jpg", "F_682.jpg", "F_683.jpg", "F_684.jpg", "F_686.jpg", "F_687.jpg",
    "F_688.jpg", "F_689.jpg", "F_69.jpg", "F_690.jpg", "F_691.jpg", "F_692.jpg", "F_693.jpg", "F_694.jpg",
    "F_695.jpg", "F_696.jpg", "F_697.jpg", "F_698.jpg", "F_699.jpg", "F_70.jpg", "F_700.jpg", "F_701.jpg",
    "F_702.jpg", "F_703.jpg", "F_704.jpg", "F_705.jpg", "F_706.jpg", "F_707.jpg", "F_708.jpg", "F_709.jpg",
    "F_71.jpg", "F_710.jpg", "F_711.jpg", "F_712.jpg", "F_713.jpg", "F_714.jpg", "F_715.jpg", "F_716.jpg",
    "F_717.jpg", "F_718.jpg", "F_719.jpg", "F_72.jpg", "F_720.jpg", "F_721.jpg", "F_723.jpg", "F_724.jpg",
    "F_725.jpg", "F_726.jpg", "F_727.jpg", "F_728.jpg", "F_729.jpg", "F_73.jpg", "F_730.jpg", "F_731.jpg",
    "F_732.jpg", "F_733.jpg", "F_734.jpg", "F_735.jpg", "F_736.jpg", "F_737.jpg", "F_738.jpg", "F_739.jpg",
    "F_74.jpg", "F_740.jpg", "F_741.jpg", "F_742.jpg", "F_743.jpg", "F_744.jpg", "F_745.jpg", "F_746.jpg",
    "F_747.jpg", "F_748.jpg", "F_749.jpg", "F_75.jpg", "F_750.jpg", "F_751.jpg", "F_752.jpg", "F_753.jpg",
    "F_754.jpg", "F_755.jpg", "F_756.jpg", "F_757.jpg", "F_758.jpg", "F_759.jpg", "F_76.jpg", "F_760.jpg",
    "F_761.jpg", "F_762.jpg", "F_763.jpg", "F_764.jpg", "F_765.jpg", "F_766.jpg", "F_767.jpg", "F_768.jpg",
    "F_769.jpg", "F_77.jpg", "F_770.jpg", "F_771.jpg", "F_772.jpg", "F_773.jpg", "F_774.jpg", "F_775.jpg",
    "F_776.jpg", "F_777.jpg", "F_778.jpg", "F_779.jpg", "F_780.jpg", "F_781.jpg", "F_782.jpg", "F_783.jpg",
    "F_784.jpg", "F_785.jpg", "F_786.jpg", "F_787.jpg", "F_788.jpg", "F_789.jpg", "F_790.jpg", "F_791.jpg",
    "F_792.jpg", "F_793.jpg", "F_794.jpg", "F_795.jpg", "F_796.jpg", "F_797.jpg", "F_798.jpg", "F_799.jpg",
    "F_80.jpg", "F_800.jpg", "F_801.jpg", "F_802.jpg", "F_803.jpg", "F_804.jpg", "F_805.jpg", "F_806.jpg",
    "F_807.jpg", "F_808.jpg", "F_809.jpg", "F_81.jpg", "F_810.jpg", "F_811.jpg", "F_812.jpg", "F_813.jpg",
    "F_814.jpg", "F_815.jpg", "F_816.jpg", "F_817.jpg", "F_818.jpg", "F_819.jpg", "F_82.jpg", "F_820.jpg",
    "F_821.jpg", "F_822.jpg", "F_823.jpg", "F_824.jpg", "F_825.jpg", "F_826.jpg", "F_827.jpg", "F_828.jpg",
    "F_829.jpg", "F_83.jpg", "F_830.jpg", "F_831.jpg", "F_832.jpg", "F_833.jpg", "F_834.jpg", "F_835.jpg",
    "F_836.jpg", "F_837.jpg", "F_838.jpg", "F_839.jpg", "F_84.jpg", "F_840.jpg", "F_841.jpg", "F_842.jpg",
    "F_843.jpg", "F_844.jpg", "F_845.jpg", "F_846.jpg", "F_847.jpg", "F_848.jpg", "F_849.jpg", "F_85.jpg",
    "F_850.jpg", "F_851.jpg", "F_852.jpg", "F_853.jpg", "F_854.jpg", "F_855.jpg", "F_856.jpg", "F_857.jpg",
    "F_858.jpg", "F_859.jpg", "F_86.jpg", "F_860.jpg", "F_861.jpg", "F_862.jpg", "F_863.jpg", "F_864.jpg",
    "F_865.jpg", "F_866.jpg", "F_867.jpg", "F_868.jpg", "F_869.jpg", "F_87.jpg", "F_870.jpg", "F_871.jpg",
    "F_872.jpg", "F_873.jpg", "F_874.jpg", "F_875.jpg", "F_876.jpg", "F_877.jpg", "F_878.jpg", "F_879.jpg",
    "F_88.jpg", "F_880.jpg", "F_881.jpg", "F_882.jpg", "F_883.jpg", "F_884.jpg", "F_885.jpg", "F_886.jpg",
    "F_887.jpg", "F_888.jpg", "F_889.jpg", "F_89.jpg", "F_890.jpg", "F_891.jpg", "F_892.jpg", "F_893.jpg",
    "F_894.jpg", "F_895.jpg", "F_896.jpg", "F_897.jpg", "F_898.jpg", "F_899.jpg", "F_90.jpg", "F_900.jpg",
    "F_901.jpg", "F_902.jpg", "F_903.jpg", "F_904.jpg", "F_905.jpg", "F_906.jpg", "F_907.jpg", "F_908.jpg",
    "F_909.jpg", "F_91.jpg", "F_910.jpg", "F_911.jpg", "F_912.jpg", "F_913.jpg", "F_914.jpg", "F_915.jpg",
    "F_916.jpg", "F_917.jpg", "F_918.jpg", "F_919.jpg", "F_92.jpg", "F_920.jpg", "F_921.jpg", "F_922.jpg",
    "F_923.jpg", "F_924.jpg", "F_925.jpg", "F_926.jpg", "F_927.jpg", "F_928.jpg", "F_929.jpg", "F_93.jpg",
    "F_930.jpg", "F_931.jpg", "F_932.jpg", "F_933.jpg", "F_934.jpg", "F_935.jpg", "F_936.jpg", "F_937.jpg",
    "F_938.jpg", "F_939.jpg", "F_94.jpg", "F_940.jpg", "F_941.jpg", "F_942.jpg", "F_943.jpg", "F_944.jpg",
    "NF_1003.jpg"
]


# Loop through the files and delete them if they exist
for filename in files_to_delete:
    file_path = os.path.join(directory_path, filename)
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted {filename}")
        else:
            print(f"{filename} does not exist in the directory")
    except Exception as e:
        print(f"Error deleting {filename}: {e}")
